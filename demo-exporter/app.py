#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import random
import sys
import yaml

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer

"""
Prometheus demo exporter
"""

PORT = 8080
URL = '0.0.0.0'
CONFIG_FILE = 'example.yml'


class ExportsHandler(BaseHTTPRequestHandler):
    global config

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        for m in config['metrics']:
            for d in m['aws_dimensions']:
                line = "{name}{{dimension=\"{dimension}\"}} {value}\n".format(
                    name=m['aws_metric_name'], dimension=d,
                    value=random.randint(1, 420) / 100.0)
                self.wfile.write(line.encode('utf8'))


def read_config(filename):
    with open(filename, 'r') as stream:
        return yaml.load(stream)


def run(server_class=HTTPServer, handler_class=ExportsHandler, port=PORT):
    server_address = (URL, port)
    httpd = server_class(server_address, handler_class)

    print('Starting Prometheus Exporter ... (use Ctrl-C to exit)')
    httpd.serve_forever()


if __name__ == "__main__":
    # parse command line args
    parser = argparse.ArgumentParser(description='Prometheus Exporter.')
    parser.add_argument('--config', dest='config', default=CONFIG_FILE,
                        help='config file')
    parser.add_argument('--port', dest='port', default=PORT,
                        help='server port')
    args = parser.parse_args()

    # read config file
    try:
        config = read_config(args.config)
    except Exception as e:
        print(e)
        sys.exit(1)

    # run server
    try:
        run(port=int(args.port))
    except KeyboardInterrupt:
        sys.exit(1)
