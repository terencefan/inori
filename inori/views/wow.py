# -*- coding:utf-8 -*-

from flask import Module
wow = Module(__name__)

from flask import (
    render_template,
)


@wow.route('/')
@wow.route('/index')
def index():
    return render_template('wow/index.html')
