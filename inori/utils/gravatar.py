#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import urllib
import hashlib

# Set your variables here
email = "stdrickforce@gmail.com"
default = "http://www.example.com/default.jpg"
size = 40

# construct the url
gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
gravatar_url += urllib.urlencode({
    'd': default,
    's': '200'
})
print gravatar_url
