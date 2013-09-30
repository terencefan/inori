# -*- coding: utf-8 -*-

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
