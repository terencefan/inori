#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import requests
import urlparse

from flask import (
    jsonify,
    request,
)

from scrapy.selector import Selector

from inori.models import Link

from inori.utils import datetime2utc


def query():

    def _links(links):
        for link in links:
            yield {
                'id': str(link.id),
                'title': link.title,
                'url': link.url,
                'icon': link.icon,
                'created_at': datetime2utc(link.created_at),
            }

    links = Link.objects().order_by('-created_at')

    return jsonify({
        'data': {
            'links': list(_links(links)),
        },
        'msg': 'success',
        'code': 200,
    })


def add():

    url = request.json.get('url', '')

    parse = urlparse.urlparse(url)

    response = requests.get(url)
    selector = Selector(text=response.content)

    title = selector.css('title').xpath('text()').extract()[0]

    link = Link(
        title=title,
        url=url,
        icon='http://{}/favicon.ico'.format(parse.hostname),
    )
    link.save()
