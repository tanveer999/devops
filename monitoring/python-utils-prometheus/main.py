from prometheus_api_client import PrometheusConnect
from prometheus_client import Gauge, start_http_server
import time

# Initialize Prometheus client
prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

# Create a custom Gauge metric to export the request count
custom_request_count = Gauge('custom_prometheus_api_requests_total', 
                           'Total number of requests to Prometheus API query endpoint',
                           ['handler', 'instance', 'job'])

def collect_and_export_metrics():
    """Collect metrics from Prometheus and export as custom metrics"""
    try:
        # Query the original metric
        output = prom.custom_query(query="prometheus_http_request_duration_seconds_count{handler=\"/api/v1/query\"}")
        
        if output:
            print(f"Original output: {output}")
            
            # Extract the request count value
            request_count = float(output[0]['value'][1])
            print(f"Request count: {request_count}")
            
            # Extract labels from the original metric
            labels = output[0]['metric']
            handler = labels.get('handler', '/api/v1/query')
            instance = labels.get('instance', 'localhost:9090')
            job = labels.get('job', 'prometheus')
            
            # Set the custom metric with the extracted value and labels
            custom_request_count.labels(handler=handler, instance=instance, job=job).set(request_count)
            
            print(f"Updated custom metric: custom_prometheus_api_requests_total = {request_count}")
        else:
            print("No data received from Prometheus query")
            
    except Exception as e:
        print(f"Error collecting metrics: {e}")

if __name__ == "__main__":
    # Start the Prometheus metrics HTTP server on port 8000
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    print("Metrics available at: http://localhost:8000/metrics")
    
    # Collect and export metrics in a loop
    while True:
        collect_and_export_metrics()
        time.sleep(30)  # Update every 30 seconds