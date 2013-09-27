# -*- coding:utf-8 -*-

from flask import Module
home = Module(__name__)

from sqlalchemy.exc import SQLAlchemyError

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.models.home import (
    DBSession,
    # models
    Blog,
    BlogCategory,
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

    blocks = []

    for user, tweet in results:
        block = tweet
        setattr(block, 'user', user)
        setattr(block, 'block_type', 'tweet')
        blocks.append(block)

    var = {
        'blocks': blocks,
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
