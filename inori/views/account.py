# -*- coding:utf-8 -*-

from flask import Module
account = Module(__name__)

from flask import (
    redirect,
    request,
    session,
    url_for,
)

from inori.models import (
    DBSession,
    User,
)

from inori.logger import logger
from inori.validator import (
    EMAIL,
    PASSWORD,
    STR,
    validate
)


@account.route('/signup', methods=['GET', 'POST'])
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

    user = User(email, password, nickname)
    print user

    return redirect(url_for('home.index'))


@account.route('/signin', methods=['GET', 'POST'])
@validate({
    'username': STR,
    'password': STR,
})
def signin():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        dbsession = DBSession()
        user = dbsession.query(User).\
            filter(User.email == username).\
            filter(User.password == password).\
            first()

        if user:
            session['logged_in'] = True
            session['user'] = {
                "id": user.id,
                "email": user.email,
                "nickname": user.nickname,
                "is_super_admin": user.is_super_admin,
            }
            logger.info(user.welcome_info)
            return redirect(url_for('home.index'))
        else:
            logger.error_code(logger.USER_AUTH_FAILED)
    else:
        logger.error_unknown()

    return redirect(url_for('home.index'))


@account.route('/signout', methods=['GET', 'POST'])
@validate({})
def signout():
    session.pop('logged_in', None)
    session.pop('user', None)
    logger.info(u'您已经成功注销了用户')
    return redirect(url_for('home.index'))
