# Install steps
helm repo add kubetail https://kubetail-org.github.io/helm-charts/
helm install kubetail kubetail/kubetail --namespace kubetail-system --create-namespace

# To access dashboard
kubectl port-forward -n kubetail-system svc/kubetail-dashboard 8080:8080
