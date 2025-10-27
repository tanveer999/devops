from fastapi import FastAPI, HTTPException
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_api_client import PrometheusConnect
from starlette.responses import Response
import logging
import asyncio
import uvicorn
from contextlib import asynccontextmanager
import signal
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Prometheus setup
prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)
custom_metric = Gauge(
    'custom_prometheus_api_requests_total',
    'Custom metric showing Prometheus API request count',
    ['handler', 'instance', 'job']
)

# Background task control
background_task = None
shutdown_event = asyncio.Event()

async def update_metrics():
    """Background task to update metrics periodically"""
    while not shutdown_event.is_set():
        try:
            query = 'prometheus_http_request_duration_seconds_count{handler="/api/v1/query"}'
            result = prom.custom_query(query=query)
            
            if result:
                for item in result:
                    metric_data = item['metric']
                    value = float(item['value'][1])
                    
                    handler = metric_data.get('handler', '')
                    instance = metric_data.get('instance', '')
                    job = metric_data.get('job', '')
                    
                    custom_metric.labels(handler=handler, instance=instance, job=job).set(value)
                    logger.info(f"Updated metric: {handler} = {value}")
            else:
                logger.warning("No data returned from Prometheus query")
                
        except Exception as e:
            logger.error(f"Error updating metrics: {e}")
        
        try:
            await asyncio.wait_for(shutdown_event.wait(), timeout=30.0)
            break
        except asyncio.TimeoutError:
            continue

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global background_task
    logger.info("Starting metrics collection...")
    background_task = asyncio.create_task(update_metrics())
    
    yield
    
    # Shutdown
    logger.info("Shutting down metrics collection...")
    shutdown_event.set()
    if background_task:
        await background_task

app = FastAPI(
    title="Prometheus Metrics Exporter",
    description="Custom Prometheus metrics exporter with FastAPI",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "healthy", "service": "prometheus-metrics-exporter"}

@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        # Test Prometheus connectivity
        result = prom.custom_query('up')
        if result:
            return {"status": "healthy", "prometheus": "connected"}
        else:
            raise HTTPException(status_code=503, detail="Prometheus not responding")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Health check failed: {str(e)}")

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    try:
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    except Exception as e:
        logger.error(f"Error generating metrics: {e}")
        raise HTTPException(status_code=500, detail="Error generating metrics")

if __name__ == "__main__":
    uvicorn.run(
        "fastapi_exporter:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )