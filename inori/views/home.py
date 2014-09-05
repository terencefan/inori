# -*- coding:utf-8 -*-

from flask import Module
home = Module(__name__)

from datetime import datetime, timedelta

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.models import (
    DBSession,
    Blog,
    BlogCategory,
    Tweet,
    User,
)

from inori.validator import (
    INT,
    STR,
    validate,
    active_required,
    admin_required,
)


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

TIME_AREA = [
    ('3h', '3 hours', 0, 3),
    ('6h', '6 hours', 3, 6),
    ('12h', '12 hours', 6, 12),
    ('1d', '1 day', 12, 24),
    ('3d', '3 days', 24, 72),
    ('1w', '1 week', 72, 168),
]


@home.route('/')
@home.route('/index')
def index():

    var = {'areas': []}
    now = datetime.now()

    for area in TIME_AREA:
        postfix, text, hour_s, hour_t = area

        trends = items_sort(now, hour_s, hour_t)
        if not trends:
            continue

        area = {
            'postfix': postfix,
            'text': text,
            'trends': trends,
        }
        var['areas'].append(area)

    return render_template('home/index.html', var=var)


@home.route('/tweet')
@active_required
def tweet():

    results = DBSession().query(User, Tweet).\
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
@active_required
def blog():

    bcs = DBSession().query(BlogCategory)
    results = DBSession().query(User, Blog).\
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
@admin_required
@validate({
    'content': STR,
})
def add_tweet():
    user_id = session['user']['id']
    content = request.form['content']
    print user_id, content
    return redirect(url_for('tweet'))


@home.route('/add_blog', methods=['GET', 'POST'])
@admin_required
@validate({
    'title': STR,
    'blog_category_id': INT,
    'content': STR,
})
def add_blog():
    user_id = session['user']['id']
    title = request.form['title']
    blog_category_id = request.form['blog_category_id']
    content = request.form['content']
    print user_id, title, blog_category_id, content
    return redirect(url_for('blog'))


@home.route('/add_blog_category', methods=['GET', 'POST'])
@admin_required
@validate({
    'name': STR,
})
def add_blog_category():
    name = request.form['name']
    print name
    return redirect(url_for('blog'))
