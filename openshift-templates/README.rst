Add a new Prometheus Exporter to OpenShift
==========================================

This ``.yaml`` add a new metrics exporter to OpenShift cluster.

The expoter is defined by it's container image and it's port.

Usage
=====

Create a ConfigMap containing the configuration file:

::

    oc create configmap config --from-file=config.yml

::

    oc describe configmap config

Create the new exporter ReplicationController:

::

    oc new-app -f demo-exporter.yml \
      -p APPNAME=my-exporter \
      -p EXPORTER_PORT=8080 \
      -p EXPORTER_IMAGE=docker.io/yaacov/demo-exporter:latest

Cleanup an old exporter (Remove all objects):

::

    oc process -f demo-exporter.yml \
      -p APPNAME=my-exporter \
      -p EXPORTER_PORT=8080 \
      -p EXPORTER_IMAGE=docker.io/yaacov/demo-exporter:latest | oc delete -f -
