# installing prometheus-node-exporter

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus-node-exporter prometheus-community/prometheus-node-exporter -n monitoring
```
Ref: https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-node-exporter

## Create nodeport service

```
kubectl create service nodeport prometheus-node-exporter-service --tcp=9100:9100 --dry-run=client -o yaml -n monitoring | \
sed 's/  selector:/  selector:\n    app.kubernetes.io\/instance: prometheus-node-exporter\n    app.kubernetes.io\/name: prometheus-node-exporter/' | \
kubectl apply -n monitoring -f -
```

# Installing kube-state-metrics

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install kube-state-metrics prometheus-community/kube-state-metrics -n monitoring

```
