# SPDX-License-Identifier: MIT

import jwt
import configuration


def encode(information):
    return jwt.encode(
        {'some': 'payload'},
        configuration.SECRETKEY,
        algorithm='HS256'
    )


def decode(token):
    return jwt.decode(
        token,
        configuration.SECRETKEY,
        algorithms=['HS256']
    )
