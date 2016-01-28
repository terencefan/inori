#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import functools
import httplib

from flask import (
    Blueprint,
    Response,
    jsonify,
)

from importlib import import_module

bp = Blueprint('api', __name__)

modules = {
    'link': [
        ('add', ['PUT'], '/'),
    ],
    'trend': [
        ('query', ['GET'], '/'),
    ],
}


def make_response(data=None, message='', code=200, status_code=httplib.OK):
    if isinstance(data, Response):
        return data

    response_body = {
        'code': code,
        'msg': message,
        'data': data,
    }
    response = jsonify(response_body)
    response.status_code = status_code
    return response


def init_app(app):

    def render_json(func):

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return make_response(func(*args, **kwargs))
        return wrapped

    for module_name, routes in modules.iteritems():
        module = import_module('.' + module_name, package='inori.apps.api')
        for name, methods, path in routes:
            route = '/' + module_name + path
            func = getattr(module, name)
            func_name = u'%s_%s' % (module_name, name)
            bp.add_url_rule(
                route, func_name, render_json(func), methods=methods)

    app.register_blueprint(bp, url_prefix='/api')


@bp.before_request
def before_request_hook():
    print 'before request hook'


@bp.after_request
def after_request_hook(response):
    return response
