#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""APIStar Web App."""


import apistar_peewee  # https://github.com/aachurin/apistar_peewee
from apistar.frameworks.wsgi import WSGIApp as App

from routes import routes
from settings import settings
from apistar import Component
from apistar_jwt.authentication import get_jwt
from apistar_jwt.token import JWT

from models.base import *
from models.user import User
from models.example_model import *


__version__ = "0.0.1"
__license__ = "GPLv3+"
__author__ = "???"
__email__ = "user@example.com"
__url__ = "https://example.com"


app: App = App(
    routes=routes,
    settings=settings,
    commands=apistar_peewee.commands,     # Install custom commands.
    components=apistar_peewee.components + [Component(JWT, init=get_jwt)],
)


if __name__ in '__main__':
    app.main()
