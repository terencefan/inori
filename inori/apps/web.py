#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Mon Aug 24 12:01:07 2015
# Updated At: Tue Sep 15 14:22:51 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import functools

from flask import (
    Blueprint,
)

from inori.config import (
    STATIC_DIR,
    ENV,
)

from inori.exc import (
    ServiceException,
)


bp = Blueprint('web', __name__)


class Template(object):

    _templates = {}

    @classmethod
    def content(cls, name):
        '''
        lazy load html content.
        always load from disk on dev env.
        '''
        if ENV != 'dev' and name in cls._templates:
            return cls._templates[name]

        filepath = '%s/build%s' % (STATIC_DIR, name)
        with open(filepath) as f:
            template = f.read().decode('utf-8')
            cls._templates[name] = template
        return cls._templates[name]


def view(template_name, required_login=True, code=200):

    def wrapper(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            return Template.content(template_name), code
        return wrap

    return wrapper


@view('/modules/index/403.html', code=403)
def e403(error):
    '''
    Permission Denied.
    '''


@view('/modules/index/404.html', code=404)
def e404(error):
    '''
    Resource Not Found.
    '''


MODULES = [
    ('/', '/modules/index/index.html'),
]


def init_app(app):

    for module in MODULES:
        route, path = module
        bp.add_url_rule(route, view_func=view(path)(lambda: ''))

    app.register_blueprint(bp, url_prefix='')
    app.errorhandler(403)(e403)
    app.errorhandler(404)(e404)


@bp.before_request
def before_request_hook():
    pass


@bp.errorhandler(ServiceException)
def service_exception_handler(e):
    return e.message
