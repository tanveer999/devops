# Linux system monitoring

1. Node exporter

# Apache monitoring

1. apache exporter

## Ref:
https://github.com/Lusitaniae/apache_exporter


# redis monitoring
```
docker run -d --name redis_exporter -p 9121:9121 oliver006/redis_exporter
```
---

# K8

## Prometheus

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```

```
helm install prometheus prometheus-community/prometheus --namespace monitoring
```

```
kubectl expose service prometheus-server --namespace monitoring --type=NodePort --target-port=9090 --name=prometheus-server-ext
```

## Grafana

```
helm repo add grafana https://grafana.github.io/helm-charts
```

```
helm install grafana grafana/grafana --namespace monitoring
```

```
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

```
kubectl expose service grafana --namespace monitoring --type=NodePort --target-port=3000 --name=grafana-ext
```