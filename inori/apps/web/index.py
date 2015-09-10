#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Wed Aug 26 18:53:16 2015
# Updated At: Thu Aug 27 13:11:38 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from inori.apps.web import (
    bp,
    view,
)


@bp.route('/index')
@view('/modules/index/index.html')
def index():
    user = {
        'a': 1,
        'b': 2,
    }
    haha = [1, 3, 5]

    return {
        'user': user,
        'haha': haha,
    }
