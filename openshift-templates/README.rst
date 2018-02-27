Template Examples: Exporter with and without a ServiceMonitor
=============================================================

This folder containes example templates for an exporter:

- `demo-exporter.yml </openshift-templates/demo-exporter.yml>`_ : Example template for an exporter, will automatically register to a Prometheus using kubernetes_sd_configs with role endpoints

- `demo-exporter-w-monitor.yml </openshift-templates/demo-exporter-w-monitor.yml>`_ : Example template for an exporter, will automatically deploy a ServiceMonitor for integration with `Prometheus operator <https://github.com/coreos/prometheus-operator>`_

The expoter is defined by it's container image and it's port, deployment can include a path for config files and a path for credentials.

Usage
=====

This method require this configuration and credentioals files:

- config.yml - metric definitions file
- credentials - aws credentials file
- config - aws config file

Create a ConfigMap containing the configuration file:
-----------------------------------------------------

::

    # Create config map
    oc create configmap exporter-config --from-file=config.yml

Create a Secret containing the credentials:
-------------------------------------------

::

    # Create secrets
    oc secrets new exporter-secrets config=config credentials=credentials


Using AWS CloudWatch
--------------------

::

    oc new-app -f demo-exporter-w-monitor.yml \
      -p APPNAME=aws-exporter \
      -p NAMESPACE=monitoring \
      -p EXPORTER_PORT=9106 \
      -p SECRETPATH=/root/.aws \
      -p CONFIGPATH=/config \
      -p EXPORTER_IMAGE=prom/cloudwatch-exporter

Generic Use
-----------
Create the new exporter ReplicationController:

( This assumes that we have `exporter-config` config map and `exporter-secrets` secrets. )

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
