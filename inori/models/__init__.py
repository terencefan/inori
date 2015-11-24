#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import datetime

from inori.config import (
    # db, host, port
    MONGO_SETTINGS
)

from mongoengine import (  # noqa
    connect,
    Document,
    DateTimeField,
)

# connect to mongodb.
connect(**MONGO_SETTINGS)


class TimeMixin(object):

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)


from .link import Link  # noqa
