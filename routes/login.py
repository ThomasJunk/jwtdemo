# SPDX-License-Identifier: MIT

import crypto


class Login:
    def on_get(self, req, resp):
        """Handles GET requests"""
        token = crypto.encode({'some': 'payload'})
        resp.set_cookie("token", token)
        return {"message": "logged in"}
