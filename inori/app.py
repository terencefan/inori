#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Thu Sep 10 22:16:05 2015
# Updated At: Tue Sep 15 17:08:48 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import importlib

from flask import (
    Flask,
)

from inori.config import (
    DEBUG,
    SECRET_KEY,
    STATIC_DIR,
)

MODULES = ['web']


class InoriFlask(Flask):
    pass


def init_module(app):
    for module in MODULES:
        mo = importlib.import_module('inori.apps.%s' % module)
        mo.init_app(app)


def init_others(app):
    pass


def init_config(app):
    app.config.update(
        PERMANENT_SESSION_LIFETIME=60 * 15,
        SESSION_REFRESH_EACH_REQUEST=True,
        SESSION_COOKIE_HTTPONLY=True,
    )
    app.debug = DEBUG
    app.secret_key = SECRET_KEY


def create_app():
    app = Flask(__name__, static_folder=STATIC_DIR)
    init_config(app)
    init_others(app)
    init_module(app)
    return app

app = create_app()
