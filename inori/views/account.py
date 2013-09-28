# -*- coding:utf-8 -*-

from flask import Module
account = Module(__name__)

from sqlalchemy.exc import SQLAlchemyError

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.models import (
    dbsession,
    User,
)

from inori.logger import logger
from inori.validator import (
    EMAIL,
    PASSWORD,
    STR,
    validate
)


def set_user(user):
    session['logged_in'] = True
    session['user'] = {
        'id': user.id,
        'email': user.email,
        'nickname': user.nickname,
        'is_super_admin': user.is_super_admin,
        'is_active': user.is_active,
    }
    logger.info(user.welcome_info)


@account.route('/signup', methods=['POST'])
@validate({
    'email': EMAIL,
    'nickname': STR,
    'password': PASSWORD,
    'repeat_pwd': STR,
})
def signup():

    email = request.form['email']
    nickname = request.form['nickname']
    password = request.form['password']
    repeat_pwd = request.form['repeat_pwd']

    if password != repeat_pwd:
        logger.error_code(logger.REPEAT_PWD_MISMATCH)
        return redirect(request.referrer)

    user = User(email, password, nickname)
    dbsession.add(user)

    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)
        return redirect(request.referrer)

    set_user(user)
    return redirect(request.referrer)


@account.route('/signin', methods=['POST'])
@validate({
    'account': STR,
    'password': STR,
})
def signin():

    account = request.form['account']
    password = request.form['password']

    user = dbsession.query(User).\
        filter(User.email == account).\
        first()

    if user:
        if user.authorize(password):
            set_user(user)
        else:
            logger.error_code(logger.USER_AUTH_FAILED)
    else:
        logger.error_code(logger.USER_NOT_FOUND)

    return redirect(request.referrer)


@account.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('logged_in', None)
    session.pop('user', None)
    logger.info(u'您已经成功注销了用户')
    return redirect(url_for('home.index'))


@account.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user(user_id):
    return render_template('account/user.html')
