# -*- coding: utf-8 -*-

from flask import (
    redirect,
    request,
    session,
    url_for,
)

from sqlalchemy.exc import SQLAlchemyError

from inori.logger import logger
from inori.models import dbsession


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


def set_user(user):

    session['logged_in'] = True
    session['user'] = {
        'id': user.id,
        'email': user.email,
        'nickname': user.nickname,
        'is_super_admin': user.is_super_admin,
        'is_active': user.is_active,
    }
