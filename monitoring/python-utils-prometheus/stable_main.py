from prometheus_api_client import PrometheusConnect
from prometheus_client import Gauge, start_http_server, Info
import time
import signal
import sys
import logging
from typing import Optional
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PrometheusMetricsExporter:
    def __init__(self, prometheus_url: str = "http://localhost:9090", metrics_port: int = 8000):
        self.prometheus_url = prometheus_url
        self.metrics_port = metrics_port
        self.running = True
        self.prom = None
        self.retry_count = 0
        self.max_retries = 3
        self.retry_delay = 5
        
        # Metrics
        self.custom_request_count = Gauge(
            'custom_prometheus_api_requests_total', 
            'Total number of requests to Prometheus API query endpoint',
            ['handler', 'instance', 'job']
        )
        
        self.service_info = Info(
            'custom_metrics_exporter',
            'Information about the custom metrics exporter'
        )
        
        self.health_metric = Gauge(
            'custom_metrics_exporter_health',
            'Health status of the custom metrics exporter (1=healthy, 0=unhealthy)'
        )
        
        # Set service info
        self.service_info.info({
            'version': '1.0',
            'prometheus_url': prometheus_url,
            'metrics_port': str(metrics_port)
        })
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)
        
    def _signal_handler(self, signum, frame):
        logger.info(f"Received signal {signum}. Shutting down gracefully...")
        self.running = False
        
    def _initialize_prometheus_client(self) -> bool:
        """Initialize Prometheus client with retry logic"""
        try:
            self.prom = PrometheusConnect(url=self.prometheus_url, disable_ssl=True)
            # Test connection
            self.prom.custom_query("up")
            logger.info(f"Successfully connected to Prometheus at {self.prometheus_url}")
            self.retry_count = 0
            return True
        except Exception as e:
            self.retry_count += 1
            logger.error(f"Failed to connect to Prometheus (attempt {self.retry_count}/{self.max_retries}): {e}")
            if self.retry_count < self.max_retries:
                logger.info(f"Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
                return self._initialize_prometheus_client()
            else:
                logger.error("Max retries reached. Unable to connect to Prometheus.")
                self.health_metric.set(0)
                return False
                
    def _collect_metrics(self) -> bool:
        """Collect and update metrics with error handling"""
        try:
            if not self.prom:
                if not self._initialize_prometheus_client():
                    return False
                    
            # Query the original metric
            query = 'prometheus_http_request_duration_seconds_count{handler="/api/v1/query"}'
            output = self.prom.custom_query(query=query)
            
            if not output:
                logger.warning("No data received from Prometheus query")
                return False
                
            # Extract and process data
            metric_data = output[0]
            request_count = float(metric_data['value'][1])
            labels = metric_data['metric']
            
            handler = labels.get('handler', '/api/v1/query')
            instance = labels.get('instance', 'localhost:9090')
            job = labels.get('job', 'prometheus')
            
            # Update custom metric
            self.custom_request_count.labels(
                handler=handler, 
                instance=instance, 
                job=job
            ).set(request_count)
            
            # Update health metric
            self.health_metric.set(1)
            
            logger.info(f"Updated metric: custom_prometheus_api_requests_total = {request_count}")
            return True
            
        except Exception as e:
            logger.error(f"Error collecting metrics: {e}")
            self.health_metric.set(0)
            self.prom = None  # Reset connection to trigger reconnect
            return False
            
    def run(self):
        """Main run loop with improved error handling"""
        try:
            # Start HTTP server
            start_http_server(self.metrics_port)
            logger.info(f"Prometheus metrics server started on port {self.metrics_port}")
            logger.info(f"Metrics available at: http://localhost:{self.metrics_port}/metrics")
            
            # Initialize Prometheus connection
            if not self._initialize_prometheus_client():
                logger.error("Failed to initialize Prometheus connection. Exiting.")
                return
                
            # Main collection loop
            while self.running:
                try:
                    self._collect_metrics()
                    # Sleep with interrupt checking
                    for _ in range(30):  # 30 seconds total
                        if not self.running:
                            break
                        time.sleep(1)
                        
                except KeyboardInterrupt:
                    logger.info("Received keyboard interrupt")
                    break
                except Exception as e:
                    logger.error(f"Unexpected error in main loop: {e}")
                    time.sleep(10)  # Wait before retrying
                    
        except Exception as e:
            logger.error(f"Fatal error: {e}")
        finally:
            logger.info("Shutting down metrics exporter")
            self.health_metric.set(0)

def main():
    """Main entry point"""
    exporter = PrometheusMetricsExporter()
    
    try:
        exporter.run()
    except Exception as e:
        logger.error(f"Failed to start exporter: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
