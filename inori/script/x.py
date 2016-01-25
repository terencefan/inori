#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Sat Sep 19 17:56:23 2015
# Updated At: Sat Sep 19 19:21:11 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import collections
import json
import os
import requests
import urllib
import urlparse

from scrapy.selector import Selector

from StringIO import StringIO

from PIL import Image


def get_image(url):

    def _transfer(url):
        slices = ['http:/']
        parse = urlparse.urlparse(url)

        slices.append(parse.netloc)
        slices.append('img-original/img')

        items = parse.path.split('/')
        slices += items[-7:-1]      # datetime

        items = items[-1].split('_')
        uid = items[0]
        slices.append('_'.join(items[:2]))
        url = '/'.join(slices)

        referer = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=%s' % uid  # noqa

        return url, referer

    url, referer = _transfer(url)

    headers = {'referer': referer}
    for ext in ['jpg', 'png']:
        r = requests.get('%s.%s' % (url, ext), headers=headers)
        if r.status_code == 200:
            return Image.open(StringIO(r.content))


def main():

    def fetch_by_item(item):

        def _transfer(url):
            parse = urlparse.urlparse(url)

            slices = ['http:/']
            slices.append(parse.netloc)
            slices.append('img-original/img')

            items = parse.path.split('/')
            slices += items[-7:-1]      # datetime

            ext = items[-1].split('.')[-1]

            items = items[-1].split('_')
            slices.append('_'.join(items[:2]))
            url = '/'.join(slices)

            return url, ext

        # Referer.
        params = {
            'mode': 'medium',
            'illust_id': item['illust_id'],
        }
        url = 'http://www.pixiv.net/member_illust.php'
        referer = url + '?' + urllib.urlencode(params)

        # Image Url.
        urlbase, ext = _transfer(item['url'])
        image_url = urlbase + '.' + ext

        # Filename.
        filename = '{:0>3d}.{}'.format(item['rank'], ext)

        # Get Image.
        headers = {'referer': referer}
        r = requests.get(image_url, headers=headers)
        return Image.open(StringIO(r.content)), filename

    mode, date = 'daily', '20160111'

    dirpath = '_'.join([mode, date])
    os.mkdir(dirpath)

    params = {
        'mode': mode,
        'date': date,
        'p': 0,
        'format': 'json',
    }
    url = 'http://www.pixiv.net/ranking.php'

    s = collections.OrderedDict()
    for i in range(11):
        params['p'] = i + 1
        r = requests.get(url, params)
        for item in json.loads(r.content)['contents']:
            image, filename = fetch_by_item(item)
            image.save(dirpath + '/' + filename)

    for key, val in s.iteritems():
        print key, val

    # sections = Selector(text=r.content).xpath('//section')
    # for index, section in enumerate(sections):
    #     print section.xpath('//h2/a/text()').extract()


if __name__ == '__main__':
    main()
