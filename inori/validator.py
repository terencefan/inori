# -*- coding: utf-8 -*-
import re

from flask import request, redirect
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
                return redirect(request.referrer)
            return function()
        return wrapped
    return wrap
