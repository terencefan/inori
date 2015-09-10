#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Mon Aug 24 12:01:07 2015
# Updated At: Thu Sep 10 23:18:59 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import functools

from flask import (
    Blueprint,
    render_template_string,
)

from flask.ext.login import login_required

from inori.config import (
    STATIC_DIR,
    ENV,
)

from inori.exc import (
    ServiceException,
)


bp = Blueprint('web', __name__, template_folder='static')


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
        with open(STATIC_DIR + name) as f:
            cls._templates[name] = render_template_string(
                f.read().decode('utf-8'))
        return cls._templates[name]

    @classmethod
    def render(cls, template_name, **context):
        '''
        append context to the end of html content.
        will write in js global vars.
        '''
        content = cls.content(template_name)
        items = ['<script>']
        for key, val in context.iteritems():
            if isinstance(val, unicode) or isinstance(val, str):
                val = "'%s'" % val
            items.append('var %s = %s' % (key, val))
        items.append('</script>')
        content += '\n'.join(items)
        return content


def view(template_name, required_login=True):
    '''
    follow the bottle usage.
    '''

    def wrapper(func):

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            context = func(*args, **kwargs) or {}
            return Template.render(template_name, **context)

        if required_login:
            wrap = login_required(wrap)
        return wrap

    return wrapper


@view('/modules/errors/403.html', required_login=False)
def e403(error):
    '''
    Permission Denied.
    '''


@view('/modules/errors/404.html', required_login=False)
def e404(error):
    '''
    Resource Not Found.
    '''


def init_app(app):
    app.register_blueprint(bp, url_prefix='/web')
    app.errorhandler(403)(e403)
    app.errorhandler(404)(e404)


@bp.before_request
def before_request_hook():
    pass


@bp.errorhandler(ServiceException)
def service_exception_handler(e):
    return e.message


from .index import *  # noqa
