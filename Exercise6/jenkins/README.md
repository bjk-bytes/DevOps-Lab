# Jenkins job for Exercise 6

The pipeline job used in Exercise 6 is defined by [../Jenkinsfile](../Jenkinsfile).

It is registered in Jenkins as a Pipeline job named
`Delivery-Monitoring-Pipeline` and runs health checks against the
monitoring stack (delivery metrics endpoint, Prometheus health and
targets, Grafana health, loaded alert rules, and a sample Prometheus
query). See the top-level [`README.md`](../README.md) for the end-to-end
walk-through.
