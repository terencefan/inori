# -*- coding: utf-8 -*-
import base64
import json

from flask import (
    redirect,
    request,
    session,
    url_for,
)

from sqlalchemy.exc import SQLAlchemyError

from inori.logger import logger
from inori.models import (
    dbsession,
    EmailSend,
)


from rsa_utils import rsa_helper


def dbcommit():
    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)
        return redirect_back()


def redirect_back():
    if request.referrer:
        return redirect(request.referrer)
    else:
        return redirect(url_for('home.index'))


def send_email(to_email, title, content):
    email_send = EmailSend(to_email, title, content)
    dbsession.add(email_send)

    try:
        dbsession.commit()
        return True
    except:
        return False


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

    message = json.dumps(params)
    message = rsa_helper.encrypt(message)
    return base64.encodestring(message)


def unpack_params(message):
    message = base64.decodestring(message)
    message = rsa_helper.decrypt(message)
    return json.loads(message)
