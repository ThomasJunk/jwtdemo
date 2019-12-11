# SPDX-License-Identifier: MIT
"""Guarding for login
Raises:
    falcon.HTTPUnauthorized: In case the user is not logged in
"""
import falcon
import crypto


def login_required(req, resp, resource, params):
    """Checks whether user is logged in
    Args:
        req (object): Request
        resp (object): Response
        resource (object): Ressource accessed
        params (object): Params
    """
    token = req.get_cookie_values('token')
    try:
        result = crypto.decode(token)
        req.context.user = "user"
        return
    except Exception as ex:
        raise falcon.HTTPUnauthorized("User is not logged in")
