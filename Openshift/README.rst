Add a new Prometheus Exporter to OpenShift
==========================================

This ``.yaml`` add a new metrics exporter to OpenShift cluster.

The expoter is defined by it's container image and it's port.

Cavets
======

a. Metrics exported to all with access prevelages (like all metrics in cluster)
b. In this example schema is always "http"

Usage
=====

Remove old exporter:

::

    oc process -f demo-exporter.yml \
      -p APPNAME=my-exporter \
      -p EXPORTER_PORT=8080 \
      -p EXPORTER_IMAGE=docker.io/yaacov/demo-exporter:latest | oc delete -f -

Create a new exporter:

::

    oc new-app -f demo-exporter.yml \
      -p APPNAME=my-exporter \
      -p EXPORTER_PORT=8080 \
      -p EXPORTER_IMAGE=docker.io/yaacov/demo-exporter:latest
