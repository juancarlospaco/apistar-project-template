#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Settings for APIStar, a simple dict."""


from apistar.parsers import JSONParser, MultiPartParser
# from apistar.permissions import IsAuthenticated
from apistar.renderers import HTMLRenderer, JSONRenderer
# from apistar_jwt.authentication import JWTAuthentication
# https://github.com/juancarlospaco/apistar-msgpack & https://msgpack.org
from apistar_msgpack import MessagePackParser, MessagePackRenderer

from permissions import *


settings: dict = {

    'DATABASE': {
        # 'default': {  # Prod.
        #     'database': 'production',
        #     'host': '127.0.0.1',
        #     'port': 5433,
        #     'user': 'user',
        #     'password': 'password',
        #     'engine': 'PooledPostgresqlDatabase',
        #     'fields': {'varchar': 'varchar'},  # Other args for DB Driver.
        #     'register_hstore': False,
        # },
        'default': {  # Development, Local, Testing.
            'database': 'testing.db',
            'engine': 'SqliteDatabase',
        },
    },

    'STATICS': {
        'ROOT_DIR': 'static',         # Include the 'static/' directory.
        'PACKAGE_DIRS': ['apistar'],  # Include the builtin apistar static files
    },

    'TEMPLATES': {
        'ROOT_DIR': 'templates',      # Include the 'templates/' directory.
        'PACKAGE_DIRS': ['apistar'],  # Include the built-in apistar templates.
    },

    'RENDERERS': (JSONRenderer(), MessagePackRenderer(), HTMLRenderer()),

    'PARSERS': (JSONParser(), MultiPartParser(), MessagePackParser()),
    # 'PARSERS': (JSONParser(), MultiPartParser()),  # Default.

    # 'AUTHENTICATION': (JWTAuthentication(), ),
    # 'JWT': {  # Do NOT PUSH your SECRET into version control!.
    #     'SECRET': 's0m3-l0ng-s3cr3t',  # Long randomized secret string key.
    #     'LEEWAY': 60,  # Seconds of expiration time.
    # },  # https://github.com/audiolion/apistar-jwt#usage

    # 'PERMISSIONS': (
    #     IsAuthenticated(), IsGuestUser(), IsFreeUser(), IsPremiumUser(),
    #     IsCompanyUser(), IsAdminUser(), IsTesterUser(), IsStaffUser(),
    # ),
    #
    # 'HUEY': {  # https://huey.readthedocs.io
    #     'FILENAME': 'huey_tasks_queue.db',  # File for Huey DB.
    #     'NAME': 'apistar',                  # Tasks Queue Name.
    #     "HOST": '127.0.0.1',                # Your Redis host.
    # },

}
