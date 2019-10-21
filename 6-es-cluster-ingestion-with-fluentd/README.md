# Useful links

reuse content from https://eksworkshop.com/
Look at:  
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes
- https://kubernetes.io/docs/concepts/cluster-administration/logging/
- https://docs.fluentd.org/v/0.12/articles/kubernetes-fluentd
- https://technology.amis.nl/2019/05/06/using-elasticsearch-fluentd-and-kibana-for-log-aggregation/
- https://medium.com/redbox-techblog/building-an-open-data-platform-logging-with-fluentd-and-elasticsearch-4582de868398
- https://medium.com/@carlosedp/log-aggregation-with-elasticsearch-fluentd-and-kibana-stack-on-arm64-kubernetes-cluster-516fb64025f9
- https://mherman.org/blog/logging-in-kubernetes-with-elasticsearch-Kibana-fluentd/

# Setup process

Run the following command to create a new namespace called 'kube-logging':  

```bash
kubectl create -f kube-logging.yaml
```

Run the following command to verify, the new namespace was created successfully:  

```bash
kubectl get namespaces
```

Run the following command to roll out the DaemonSet:  

```bash
kubectl create -f fluentd.yaml
```

Verify that your DaemonSet rolled out successfully:  

```bash
kubectl get ds --namespace=kube-logging
```