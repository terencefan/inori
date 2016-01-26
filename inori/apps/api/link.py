#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import requests
import urlparse

from scrapy.selector import Selector

from inori.apps.api import bp

from inori.models import Link


@bp.route('/link')
def query():
    return {
        'links': [1, 2],
    }


def fetch(url):

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


if __name__ == '__main__':
    url = 'http://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/a-guide-to-pythons-magic-methods.html'  # noqa
    fetch(url)
