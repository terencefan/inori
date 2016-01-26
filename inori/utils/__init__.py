#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Thu Sep 10 22:15:32 2015
# Updated At: Thu Sep 10 22:15:32 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import datetime
import time


def datetime2utc(dt, scale=1000):
    return int(time.mktime(dt.timetuple()) * scale)


def utc2datetime(ts):
    return datetime.datetime.fromtimestamp(ts)
