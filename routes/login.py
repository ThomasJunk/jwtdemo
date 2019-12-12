# SPDX-License-Identifier: MIT

import crypto
import configuration


class Login:
    def on_get(self, req, resp):
        """Handles GET requests"""
        token = crypto.encode({'some': 'payload'}).decode('utf-8')
        resp.set_cookie("token", token, secure=configuration.SECURE_COOKIE)
        return {"message": "logged in"}
