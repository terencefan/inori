# -*- coding: utf-8 -*-

from flask import session

from sqlalchemy.exc import SQLAlchemyError

from inori.logger import logger
from inori.models import dbsession
from inori.validator import redirect_back


def dbcommit():
    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)
        return redirect_back()


def set_user(user, has_info=True):

    session['logged_in'] = True
    session['user'] = {
        'id': user.id,
        'email': user.email,
        'nickname': user.nickname,
        'is_super_admin': user.is_super_admin,
        'is_active': user.is_active,
    }
    if has_info:
        logger.info(user.welcome_info)
