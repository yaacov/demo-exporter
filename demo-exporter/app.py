#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

"""
Prometheus demo exporter
"""
try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
URL = '0.0.0.0'
METRICS = [
    {'name': 'metric', 'tags': 'tag="hello"'},
    {'name': 'metric', 'tags': 'tag="world"'},
    {'name': 'events', 'tags': 'tag="hello"'},
    {'name': 'events', 'tags': 'tag="world"'},
]


class ExportsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        for m in METRICS:
            line = "{name}{{{tags}}} {value}\n".format(
                name=m['name'], tags=m['tags'],
                value=random.randint(1, 420) / 100.0)
            self.wfile.write(line.encode('utf8'))


def run(server_class=HTTPServer, handler_class=ExportsHandler, port=PORT):
    server_address = (URL, port)
    httpd = server_class(server_address, handler_class)

    print('Starting Prometheus Exporter...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
