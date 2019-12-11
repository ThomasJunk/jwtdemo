# SPDX-License-Identifier: MIT


class Login:
    def on_get(self, req, resp):
        """Handles GET requests"""
        return {"message": "logged in"}
