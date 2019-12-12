# SPDX-License-Identifier: MIT

import falcon
import middleware


class Content:
    @falcon.before(middleware.authenticated)
    def on_get(self, req, resp):
        return {"content": "secrets"}
