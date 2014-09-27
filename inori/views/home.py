# -*- coding:utf-8 -*-

from flask import Module
home = Module(__name__)

from flask import (
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from inori.validator import (
    INT,
    STR,
    validate,
    active_required,
    admin_required,
)


TIME_AREA = [
    ('3h', '3 hours', 0, 3),
    ('6h', '6 hours', 3, 6),
    ('12h', '12 hours', 6, 12),
    ('1d', '1 day', 12, 24),
    ('3d', '3 days', 24, 72),
    ('1w', '1 week', 72, 168),
]


@home.route('/')
@home.route('/timeline')
def timeline():
    return render_template('home/timeline.html')


@home.route('/tweet')
@active_required
def broadcast():
    return render_template('home/broadcast.html')


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
