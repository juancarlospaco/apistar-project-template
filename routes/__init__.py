#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Routes for APIStar, a Tuple with Routes maps URLs, Methods to Functions."""


from apistar import Include, Route
from apistar.handlers import docs_urls
from apistar.handlers import serve_static

from views import *


routes: tuple = (

    Include('/docs', docs_urls),  # Documentation autogenerated at /docs/

    Route('/static/{path}', 'GET', serve_static),  # Static files from /static/

    Route('/', 'GET', index),

    Route('/debug_request', 'GET', debug_request),

)
