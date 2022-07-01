# PROMETHEUS MONITORING DEMO
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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


This repo contains everything you need to get started with modern monitoring with prometheus and Grafana!

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

1. A containerized flask web app.
2. A containerized Prometheus server.
3. A containerized Grafana instance.

The web app UI can be visualized at `http://localhost:8887`:
![alt_text](https://github.com/R3DRUN3/prometheus-demo/blob/main/Images/webapp.png)

Prometheus web UI can be visualized at `http://localhost:9090` while Grafana at `http://localhost:3000`

Note that the Flask Web app expose a `/metrics` endpoint:
![alt_text](https://github.com/R3DRUN3/prometheus-demo/blob/main/Images/metrics.png)
this is the default endpoint that Prometheus will scrape.
<br>
Prometheus implements a pull engine in which the server scrapes the specified enpoints to gather required metrics.

Refresh the web app url to register some metrics (this project make use of [Prometheus Flask Exporter](https://github.com/rycus86/prometheus_flask_exporter)).

At this point you can login on the Grafana Web UI with the credentials that you find in `docker-compose.yml`.
<br>
Go to `add data source`, select `Prometheus` (the first one) and in the url type `http:prometheus:9090` and save.
Now is time to create our dashboard.
<br>
Go to dashboard and import the json in `grafana/dashboards`.
You should see the following dashboard:
![alt_text](https://github.com/R3DRUN3/prometheus-demo/blob/main/Images/graphana-dashboard.png)

This dashboard collects the following metrics:

1. Scrape duration (seconds).
2. Web App Cpu Usage (seconds).
3. Total http request to the web app.

Now try to launch a stress test with the following command.
```console
sh webapp_stress_test.sh
```
and observe how all the charts changes in near real time (they will spike up).

Prometheus also posses an allerting engine therefore another test that can be done is to stop the web app container
<br>
(`docker stop <containerid>`) and verify that prometheus raises the alert:

![alt_text](https://github.com/R3DRUN3/prometheus-demo/blob/main/Images/prometheus-alert.png)

Note that this is not a production ready alert, to see how to configure a complete alerting system, see the official [docs](https://prometheus.io/docs/alerting/latest/overview/).

All this is enough to start experimenting with this technology.
The advice is to study the entire project and the various files in detail to understand how these 3 elements fit together to produce a complete monitoring stack.
<br>
Afterwards it is recommended to become familiar with Grafana and to build custom dashboards using PromQL (Prometheus query language).

