#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""APIStar Web App."""

import sys
import apistar_peewee  # https://github.com/aachurin/apistar_peewee
from apistar.frameworks.wsgi import WSGIApp as App

from routes import routes
from settings import settings
from apistar import Component
from apistar_jwt.authentication import get_jwt
from apistar_jwt.token import JWT


__version__ = "1.0.0"
__license__ = "???"
__author__ = "???"
__email__ = "user@example.com"
__url__ = "https://example.com"


sys.dont_write_bytecode = settings.get("DONT_WRITE_BYTECODE", True)  # No *.PYC


app: App = App(
    routes=routes,
    settings=settings,
    commands=apistar_peewee.commands,     # Install custom commands.
    components=apistar_peewee.components + [Component(JWT, init=get_jwt)],
)


if __name__ in '__main__':
    app.main()
