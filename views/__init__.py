#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Views for APIStar, simple Functions with Type annotations."""


from urllib import parse

from settings import settings

from apistar import annotate, http, render_template
from apistar.renderers import HTMLRenderer
from playhouse.shortcuts import model_to_dict

import apistar_peewee


def debug_request(request: http.Request):
    return {'method': str(request.method),
            'url': str(request.url),
            'body': dict(parse.parse_qs(request.body.decode("utf-8"))),
            'headers': dict(request.headers)}


@annotate(renderers=[HTMLRenderer()])
def index():
    return render_template('index.html')


@annotate(renderers=[HTMLRenderer()])
def register():
    return render_template('signin.html')


def make_user(body: http.Body, database: apistar_peewee.Session):

    body_dict = parse.parse_qs(body.decode("utf-8"))
    data = {k: v[0] for k, v in body_dict.items()}  # Clean out values.

    if isinstance(data.get("username"), str):
        username = data.get("username").strip().lower()

    new_user = database.User(
        username=username,
        password=data.get("password"),
        email=data.get("email"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        company=data.get("company"),
        bio=data.get("bio"),
        url_home=data.get("url_home"),
        bday=data.get("bday"),
        country=data.get("country", "us"),
        language=data.get("language", "en"),
    )
    new_user.save()
    print(f"Created 1 New User Account: {new_user} from {data} on {database}.")
    return model_to_dict(new_user)


@annotate(renderers=[HTMLRenderer()])
def login():
    return render_template('login.html')


def logout(session: http.Session):
    if session.data:
        for key in session.data.keys():
            del session[key]
    print(f"LOGOUT. {session.data} {session}")
    return session.data
