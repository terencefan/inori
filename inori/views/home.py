# -*- coding:utf-8 -*-

from flask import Module
home = Module(__name__)

from flask import (
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.models.home import (
    DBSession,
    Tweet,
    User,
)

home = Module(__name__)


@home.route('/')
@home.route('/index')
def index():
    dbsession = DBSession()
    tweets = dbsession.query(Tweet).\
        order_by(Tweet.created_at.desc())

    var = {
        'tweets': tweets,
    }
    return render_template('home/index.html', var=var)


@home.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    user_id = session['user']['id']
    is_super_admin = session['user']['is_super_admin']
    content = request.form['content']

    if not is_super_admin:
        return redirect(url_for('index'))

    tweet = Tweet(user_id, content)

    dbsession = DBSession()
    dbsession.add(tweet)
    dbsession.commit()

    return redirect(url_for('index'))


@home.route('/signin', methods=['GET', 'POST'])
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
            flash(u'您已经成功登陆')
            return redirect(url_for('index'))

    flash(u'用户名或密码错误')
    return redirect(url_for('index'))


@home.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect(url_for('index'))
