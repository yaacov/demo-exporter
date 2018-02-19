Add a new Prometheus Exporter to OpenShift
==========================================

This ``.yaml`` add a new metrics exporter to OpenShift cluster.

The expoter is defined by it's container image and it's port.

Usage
=====

Create a ConfigMap containing the configuration file:

::

    # Create config map
    oc create configmap exporter-config --from-file=config.yml

    # Create secrets
    oc secrets new exporter-secrets config=config credentials=credentials

::

    # Check that the configmap created successfully
    oc describe configmap exporter-config


Create the new exporter ReplicationController:
This assumes that we have:
exporter-config config map and exporter-secrets secrets

::

    oc new-app -f demo-exporter.yml \
      -p APPNAME=my-exporter \
      -p EXPORTER_PORT=8080 \
      -p EXPORTER_IMAGE=docker.io/yaacov/demo-exporter:latest

::

    # Cleanup an old exporter (Remove all objects):
    oc process -f demo-exporter.yml \
      -p APPNAME=my-exporter \
      -p EXPORTER_PORT=8080 \
      -p EXPORTER_IMAGE=docker.io/yaacov/demo-exporter:latest | oc delete -f -
