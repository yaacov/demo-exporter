Demo Exporter
=============

Demo Prometheus exporter

Running
=======
``./demo-exporter/app.py``

``curl http://localhost:8080/metrics``

Options
=======

::

    ./demo-exporter/app.py  --help
    usage: app.py [-h] [--config CONFIG] [--port PORT]

    Prometheus Exporter.

    optional arguments:
      -h, --help       show this help message and exit
      --config CONFIG  config file
      --port PORT      server port


Running as a Container
======================

::

    docker build -t yaacov/demo-exporter .
    docker tag yaacov/demo-exporter docker.io/yaacov/demo-exporter:latest
    docker push docker.io/yaacov/demo-exporter

::

    docker run -it --rm --name demo-exporter yaacov/demo-exporter
    
Getting the container ip:

::

    docker inspect demo-exporter | grep IPAddress\" | head -n1 | egrep -o '[0-9.]+'
