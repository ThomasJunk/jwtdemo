# SPDX-License-Identifier: MIT


class Content:
    def on_get(self, req, resp):
        return {"content": "secrets"}
