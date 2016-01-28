#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from collections import defaultdict

from inori.models import Link


def query():

    links = Link.objects().order_by('-created_at')

    groups = defaultdict(list)
    for link in links:
        groups[link.created_at.strftime('%Y-%m-%d')].append(link)

    result = []
    for key, val in groups.items():
        items = [x.serialize() for x in val]
        result.append({
            'key': key,
            'date': key[5:],
            'items': items,
        })
    result.sort(key=lambda x: x['key'], reverse=True)

    return {
        'groups': result
    }
