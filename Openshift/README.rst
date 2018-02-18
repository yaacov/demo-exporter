Usage
=====

Remove old exporter:

``oc process -f demo-exporter.yml -p APPNAME=my-exporter -p EXPORTER_PORT=8080 | oc delete -f -``

Create a new exporter:
``oc new-app -f demo-exporter.yml -p APPNAME=my-exporter -p EXPORTER_PORT=8080``
