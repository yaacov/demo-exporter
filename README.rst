Demo Exporter
=============

Demo Prometheus exporter

Running
=======
``./app.py``

``curl http://localhost:8080/metrics``

Running as a Container
======================

::

    docker build -t yaacov/demo-exporter .
    docker tag yaacov/demo-exporter docker.io/yaacov/demo-exporter:latest
    docker push docker.io/yaacov/demo-exporter

::

    docker run -it --rm --name demo-exporter yaacov/demo-exporter
