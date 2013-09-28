# -*- coding:utf-8 -*-

from flask import Module
home = Module(__name__)

from datetime import datetime, timedelta

from sqlalchemy.exc import SQLAlchemyError

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.models import (
    DBSession,
    # models
    Blog,
    BlogCategory,
    Tweet,
    User,
)

from inori.logger import logger


def tweet_items(now, hour_s, hour_t):
    time_s = now - timedelta(hours=hour_s)
    time_t = now - timedelta(hours=hour_t)

    results = DBSession().query(User, Tweet).\
        filter(User.id == Tweet.user_id).\
        filter(Tweet.created_at.between(time_t, time_s))

    items = []
    for user, tweet in results:
        item = tweet
        setattr(item, 'user', user)
        setattr(item, 'item_type', 'tweet')
        items.append(item)

    return items


def blog_items(now, hour_s, hour_t):
    time_s = now - timedelta(hours=hour_s)
    time_t = now - timedelta(hours=hour_t)

    results = DBSession().query(User, Blog).\
        filter(User.id == Blog.user_id).\
        filter(Blog.created_at.between(time_t, time_s))

    items = []
    for user, blog in results:
        item = blog
        setattr(item, 'user', user)
        setattr(item, 'item_type', 'blog')
        items.append(item)

    return items


def items_sort(now, hour_s, hour_t):
    items = []
    items += tweet_items(now, hour_s, hour_t)
    items += blog_items(now, hour_s, hour_t)

    return sorted(items, key=lambda a: a.created_at, reverse=True)


@home.route('/')
@home.route('/index')
def index():

    var = {}
    now = datetime.now()

    var['items_3h'] = items_sort(now, 0, 3)
    var['items_6h'] = items_sort(now, 3, 6)
    var['items_12h'] = items_sort(now, 6, 12)
    var['items_1d'] = items_sort(now, 12, 24)
    var['items_3d'] = items_sort(now, 24, 72)
    var['items_1w'] = items_sort(now, 72, 168)

    return render_template('home/index.html', var=var)


@home.route('/tweet')
def tweet():
    dbsession = DBSession()

    results = dbsession.query(User, Tweet).\
        filter(User.id == Tweet.user_id).\
        order_by(Tweet.created_at.desc())

    tweets = []

    for user, tweet in results:
        setattr(tweet, 'user', user)
        tweets.append(tweet)

    var = {
        'tweets': tweets,
    }

    return render_template('home/tweet.html', var=var)


@home.route('/blog')
def blog():

    dbsession = DBSession()

    bcs = dbsession.query(BlogCategory)
    results = dbsession.query(User, Blog).\
        filter(User.id == Blog.user_id).\
        order_by(Blog.created_at.desc())

    blogs = []

    for user, blog in results:
        setattr(blog, 'user', user)
        blogs.append(blog)

    var = {
        'bcs': bcs,
        'blogs': blogs,
    }

    return render_template('home/blog.html', var=var)


@home.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    user_id = session['user']['id']
    content = request.form['content']

    if not content:
        logger.error_code(logger.TWEET_IS_TOO_SHORT)
        return redirect(url_for('tweet'))

    tweet = Tweet(user_id, content)

    dbsession = DBSession()
    dbsession.add(tweet)

    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)

    return redirect(url_for('tweet'))


@home.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    user_id = session['user']['id']
    title = request.form['title']
    blog_category_id = request.form['blog_category_id']
    content = request.form['content']

    dbsession = DBSession()
    bc = dbsession.query(BlogCategory).get(blog_category_id)

    if not bc:
        logger.error_code(logger.BLOG_CATEGORY_NOT_FOUND)
        return redirect(url_for('blog'))

    if not title:
        logger.error_code(logger.BLOG_TITLE_IS_TOO_SHORT)
        return redirect(url_for('blog'))

    if len(content) < 15:
        logger.error_code(logger.BLOG_CONTENT_IS_TOO_SHORT)
        return redirect(url_for('blog'))

    blog = Blog(
        user_id=user_id,
        blog_category_name=bc.name,
        title=title,
        content=content,
    )

    dbsession.add(blog)

    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)

    return redirect(url_for('blog'))


@home.route('/add_blog_category', methods=['GET', 'POST'])
def add_blog_category():
    name = request.form['name']

    if not name:
        logger.error_code(logger.BLOG_CATEGORY_NAME_IS_TOO_SHORT)
        return redirect(url_for('blog'))

    blog_category = BlogCategory(name)

    dbsession = DBSession()
    dbsession.add(blog_category)

    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)

    return redirect(url_for('blog'))
