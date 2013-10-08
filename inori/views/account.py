# -*- coding:utf-8 -*-

from flask import Module
account = Module(__name__)

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.logger import logger

from inori.models import (
    dbsession,
    User,
)

from inori.utils import (
    dbcommit,
    redirect_back,
    set_user,
    send_email,
    pack_params,
)

from inori.validator import (
    EMAIL,
    PASSWORD,
    STR,
    OPTIONAL_STR,
    validate,
    own_required,
)


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

    if len(nickname) < 2:
        logger.error_code(logger.NICKNAME_IS_TOO_SHORT)
        return redirect_back()

    if password != repeat_pwd:
        logger.error_code(logger.REPEAT_PWD_MISMATCH)
        return redirect_back()

    user = User(email, password, nickname)
    dbsession.add(user)

    set_user(user)
    if user.welcome_info:
        logger.info(user.welcome_info)

    return redirect_back()


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

    if not user:
        logger.error_code(logger.USER_NOT_FOUND)

    if not user.authorize(password):
        logger.error_code(logger.USER_AUTH_FAILED)

    set_user(user)
    send_email(user.email, u'测试邮件', u'请不要回复')
    if user.welcome_info:
        logger.info(user.welcome_info)

    return redirect_back()


@account.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('logged_in', None)
    session.pop('user', None)
    logger.info(u'您已经成功注销了用户')
    return redirect(url_for('home.index'))


@account.route('/user/<int:user_id>', methods=['GET', 'POST'])
@own_required
def user(user):
    dbcommit()
    return render_template('account/user.html', user=user)


@account.route('/edit/<int:user_id>', methods=['GET', 'POST'])
@validate({
    'nickname': OPTIONAL_STR,
    'welcome_info': OPTIONAL_STR,
})
@own_required
def edit(user):

    nickname = request.form.get('nickname')
    welcome_info = request.form.get('welcome_info')

    if nickname is not None:
        if len(nickname) < 2:
            logger.error_code(logger.NICKNAME_IS_TOO_SHORT)
            return redirect(url_for('account.user', user_id=user.id))
        user.nickname = nickname
    if welcome_info is not None:
        user.welcome_info = welcome_info

    dbcommit()
    if user.id == session['user']['id']:
        set_user(user)
    return redirect(url_for('account.user', user_id=user.id))


@account.route('/active/send/<int:user_id>', methods=['GET', 'POST'])
@own_required
def active_send(user):
    string = pack_params(id=user.id, email=user.email)
    logger.info(string)
    return redirect_back()
