# -*- coding:utf-8 -*-

from flask import Module, Markup
home = Module(__name__)

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.models.home import (
    DBSession,
    Tweet,
)

from inori.models.account import (
    User,
)

from inori.logger import logger


@home.route('/')
@home.route('/index')
def index():
    dbsession = DBSession()
    results = dbsession.query(User, Tweet).\
        filter(User.id == Tweet.user_id).\
        order_by(Tweet.created_at.desc())

    tweets = []

    for user, tweet in results:
        setattr(tweet, 'nickname', user.nickname)
        setattr(tweet, 'content_text', Markup(tweet.content).striptags())
        tweets.append(tweet)

    var = {
        'tweets': tweets,
    }
    return render_template('home/index.html', var=var)


@home.route('/tweet')
def tweet():
    dbsession = DBSession()
    results = dbsession.query(User, Tweet).\
        filter(User.id == Tweet.user_id).\
        order_by(Tweet.created_at.desc())

    tweets = []

    for user, tweet in results:
        setattr(tweet, 'nickname', user.nickname)
        setattr(tweet, 'content_text', Markup(tweet.content).striptags())
        tweets.append(tweet)

    var = {
        'tweets': tweets,
    }

    return render_template('home/tweet.html', var=var)


@home.route('/blog')
def blog():
    return render_template('home/blog.html')


@home.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    user_id = session['user']['id']
    is_super_admin = session['user']['is_super_admin']
    content = request.form['content']

    if not is_super_admin:
        logger.error_code(logger.PERMISSION_DENIED)
        return redirect(url_for('tweet'))

    if len(content) < 10:
        logger.error_code(logger.TWEET_IS_TOO_SHORT)
        return redirect(url_for('tweet'))

    tweet = Tweet(user_id, content)

    dbsession = DBSession()
    dbsession.add(tweet)
    dbsession.commit()

    return redirect(url_for('tweet'))
