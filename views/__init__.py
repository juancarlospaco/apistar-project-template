#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Views for APIStar, simple Functions with Type annotations."""


from urllib import parse
from typing import *  # Type Annotations.

from schemas import *  # Schema Validators.
from settings import settings

from apistar import annotate, http, render_template
from apistar.renderers import HTMLRenderer


def debug_request(request: http.Request):
    return {'method': str(request.method),
            'url': str(request.url),
            'body': dict(parse.parse_qs(request.body.decode("utf-8"))),
            'headers': dict(request.headers)}


@annotate(renderers=[HTMLRenderer()])
def index():
    return render_template('index.html')
