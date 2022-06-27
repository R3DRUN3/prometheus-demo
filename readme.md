# PROMETHEUS MONITORING DEMO

Prometheus monitoring demo 📊 📈 📏

## Abstract 
**Prometheus** is a free software application used for event monitoring and alerting.
<br> 
It records real-time metrics in a time series database (allowing for high dimensionality) built using a HTTP pull model, with flexible queries and real-time alerting.
<br> 
The project is written in Go and licensed under the Apache 2 License, with source code available on [GitHub](https://github.com/prometheus/prometheus) and is a graduated project of the Cloud Native Computing Foundation, along with Kubernetes and Envoy.

**Grafana** is a multi-platform open source analytics and interactive visualization web application. 
<br>
It provides charts, graphs, and alerts for the web when connected to supported data sources.
As a visualization tool, Grafana is a popular component in monitoring stacks, often used in combination with time series databases such as InfluxDB, Prometheus and Graphite.


This repo contains everything you need to get started with modern monitoring with prometheus and Grafana

## Instructions
clone this repo:
```console
git clone https://github.com/R3DRUN3/prometheus-demo.git \
&& cd prometheus-demo 
```

Fire up the monitoring stack with docker-compose:
```console
docker-compose up
```
This command will fire up 3 entities:
1. A flask web app container
2. A Prometheus server container
3. A grafana server container
