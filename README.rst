Demo Exporter
=============

Demo Prometheus exporter

Simulates a Prometheus exporter with command line arguments, config file and secrets.

The `openshift-templates <https://github.com/yaacov/demo-exporter/tree/master/openshift-templates>`_ direcotry includes templates and instructions
for deployinng the exporter in an openshift cluster. 

Running
=======
``./demo-exporter/app.py --config demo-exporter/example.yml``

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
