
# Ref:
    https://github.com/Lusitaniae/apache_exporter

# Ref:
    https://machineperson.github.io/monitoring/2016/01/04/exporting-apache-metrics-to-prometheus.html

# Running as docker container

```
docker run -p 9117:9117  --rm bitnami/apache-exporter --scrape_uri="http://192.168.56.10/server-status/?auto"

```

