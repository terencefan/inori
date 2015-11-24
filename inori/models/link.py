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


class Link(Document, TimeMixin):

    name = StringField(required=True)
    href = StringField(required=True)
    image = StringField(required=True)

    @property
    def image_url(self):
        pass
