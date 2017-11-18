#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Views for APIStar, simple Functions with Type annotations."""


from typing import *  # Type Annotations.
import apistar_peewee
from apistar.http import Response
from apistar.interfaces import Auth

from schemas import *  # Schema Validators.
from settings import settings

from apistar import annotate
from apistar.interfaces import Auth
from apistar_jwt.authentication import JWTAuthentication
from apistar_jwt.token import JWT


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}
