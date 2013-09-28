# -*- coding: utf-8 -*-
import re

from flask import (
    request,
    redirect,
    session,
    url_for,
)
from functools import wraps

from inori.logger import logger

EMAIL_RE = re.compile('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')
MOBILE_RE = re.compile('1[3|4|5|8]\d{9}')
PASSWORD_RE = re.compile('[a-zA-Z0-9]{8,15}')


def check(func, value):
    try:
        func(value)
        return True
    except:
        return False


def is_email(s):
    if EMAIL_RE.match(s) is None:
        raise Exception


def is_mobile(s):
    if MOBILE_RE.match(s) is None:
        raise Exception


def is_password(s):
    if PASSWORD_RE.match(s) is None:
        raise Exception


def func_name(func, name=None, optional=False):
    return (func, name or func.__name__, optional)


def optional(formatter):
    func, name, optional = formatter
    return func_name(func, name, True)


def redirect_back():
    if request.referrer:
        return redirect(request.referrer)
    else:
        return redirect(url_for('home.index'))


BOOL = func_name(bool)
EMAIL = func_name(is_email)
FLOAT = func_name(float)
INT = func_name(int)
MOBILE = func_name(is_mobile)
PASSWORD = func_name(is_password)
STR = func_name(lambda c: c, 'str')

OPTIONAL_BOOL = optional(BOOL)
OPTIONAL_FLOAT = optional(FLOAT)
OPTIONAL_INT = optional(INT)
OPTIONAL_STR = optional(STR)


def validate(validators):
    def wrap(function):
        @wraps(function)
        def wrapped():

            has_error = False

            required = set([k for k, v in validators.items() if not v[2]])
            request_params = set(request.form.keys())
            missing_params = required - request_params

            for param in missing_params:
                logger.error(u'缺少参数{}'.format(param))
                has_error = True

            for key, val in request.form.items():
                if key not in validators:
                    continue
                func, name, optional = validators.get(key)
                if not check(func, val):
                    logger.error_format(key)
                    has_error = True

            if has_error:
                return redirect_back()
            return function()
        return wrapped
    return wrap


def login_required(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        if session.get('logged_in') and session.get('user'):
            if not session['user'].get('is_active'):
                logger.info(u'您的账号尚未被激活，请联系管理员或回答验证问题')
                return redirect_back()
            return function(*args, **kwargs)
        else:
            logger.info(u'您需要登陆后才能完成这一操作')
            return redirect_back()
    return wrapped


def admin_required(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        if session.get('logged_in') and session.get('user'):
            if not session['user'].get('is_active'):
                logger.info(u'您的账号尚未被激活，请联系管理员或回答验证问题')
                return redirect_back()
            if not session['user'].get('is_super_admin'):
                logger.error(u'您无权完成这一操作, 如有疑问请联系小祈~')
                return redirect_back()
            return function(*args, **kwargs)
        else:
            logger.info(u'您需要登陆后才能完成这一操作')
            return redirect_back()
        return function(*args, **kwargs)
    return wrapped
