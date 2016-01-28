#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from mongoengine import (
    Document,
    StringField,
)

from inori.models import (
    TimeMixin,
)

from inori.utils import datetime2utc


class Link(Document, TimeMixin):

    title = StringField(required=True)
    abstract = StringField(default='')

    url = StringField(required=True)
    icon = StringField(required=True)

    def serialize(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'url': self.url,
            'icon': self.icon,
            'created_at': datetime2utc(self.created_at),
        }
