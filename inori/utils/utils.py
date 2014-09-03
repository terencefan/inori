# -*- coding: utf-8 -*-
import base64
import json

from flask import (
    redirect,
    request,
    session,
    url_for,
)

from rsa_utils import RsaHelper


def redirect_back():
    if request.referrer:
        return redirect(request.referrer)
    else:
        return redirect(url_for('home.index'))


def set_user(user):

    session['logged_in'] = True
    session['user'] = {
        'id': user.id,
        'email': user.email,
        'nickname': user.nickname,
        'is_super_admin': user.is_super_admin,
        'is_active': user.is_active,
    }


def pack_params(**kwargs):
    params = {}
    for key, val in kwargs.items():
        params[key] = val

    rsa_helper = RsaHelper()
    message = json.dumps(params)
    message = rsa_helper.encrypt(message)
    return base64.encodestring(message)


def unpack_params(message):
    rsa_helper = RsaHelper()
    message = base64.decodestring(message)
    message = rsa_helper.decrypt(message)
    return json.loads(message)
