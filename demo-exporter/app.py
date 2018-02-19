#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import yaml

from multiprocessing import Process, Manager
try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer

from scrapper import scrapper

"""
Prometheus demo exporter
"""

PORT = 8080
URL = '0.0.0.0'
CONFIG_FILE = 'example.yml'


class ExportsHandler(BaseHTTPRequestHandler):
    global data

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        for (k, v) in dict(data).items():
            line = "{k} {v}\n".format(k=k, v=v)
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
    manager = Manager()
    data = manager.dict()

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

    p = Process(target=scrapper, args=(config, data, 30,))
    p.start()

    # run server
    try:
        run(port=int(args.port))
    except KeyboardInterrupt:
        p.join()
        sys.exit(1)
