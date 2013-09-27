# -*- coding: utf-8 -*-
from flask import session

"""
inori.logger
============

This module contains all Exception
"""


def init_session():
    keys = ['info_list', 'error_list']
    for key in keys:
        if key not in session.keys():
            session[key] = []


class InoriLogger(object):

    # SYSTEM_ERROR
    UNKNOWN_ERROR = 600
    PERMISSION_DENIED = 601

    # USER_EXCEPTION
    USER_AUTH_FAILED = 700
    TWEET_IS_TOO_SHORT = 701

    CODE_TO_MSG_MAP = {
        UNKNOWN_ERROR: u"一些奇怪的错误粗线了！",
        PERMISSION_DENIED: u"噗噗噗，这可不是你能来的地方",

        USER_AUTH_FAILED: u"看起来你输错了用户名或密码，一股弱者的气息",
        TWEET_IS_TOO_SHORT: u"好歹你也给我输十个字符吧！你不能这样！",
    }

    def info(self, msg):
        init_session()
        session['info_list'].append(msg)

    def error(self, msg):
        init_session()
        session['error_list'].append(msg)

    def info_code(self, code):
        msg = ""
        return self.info(msg)

    def error_code(self, code):
        msg = self.CODE_TO_MSG_MAP.get(code, u"一些奇怪的错误粗线了！")
        return self.error(msg)

    def error_unknown(self):
        msg = self.CODE_TO_MSG_MAP.get(self.UNKNOWN_ERROR)
        return self.error(msg)

logger = InoriLogger()
