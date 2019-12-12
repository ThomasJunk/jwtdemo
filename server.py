"""Server component
"""
# SPDX-License-Identifier: MIT

import logging
from wsgiref import simple_server

import falcon

from routes import Content, Login

app = falcon.API()

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app.add_route("/api/login", Login())
app.add_route("/api/content", Content())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
