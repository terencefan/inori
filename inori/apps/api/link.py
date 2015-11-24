#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>


from inori.apps.api import bp


@bp.route('/link')
def query():
    return {
        'links': [1, 2],
    }
