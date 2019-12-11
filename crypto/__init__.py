# SPDX-License-Identifier: MIT

import os
import jwt

SECRET = os.getenv("SECRETKEY")


def encode(information):
    return jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')


def decode(token):
    return jwt.decode(token, SECRET, algorithms=['HS256'])
