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
    TWEET_IS_TOO_SHORT = 702
    BLOG_CATEGORY_NAME_IS_TOO_SHORT = 703
    BLOG_TITLE_IS_TOO_SHORT = 704
    BLOG_CONTENT_IS_TOO_SHORT = 705
    BLOG_CATEGORY_NOT_FOUND = 706

    CODE_TO_MSG_MAP = {
        UNKNOWN_ERROR: u"一些奇怪的错误粗线了！",
        PERMISSION_DENIED: u"噗噗噗，这可不是你能来的地方",

        USER_AUTH_FAILED: u"看起来就是输错邮箱或密码了，一股弱者的气息",
        TWEET_IS_TOO_SHORT: u"是不可以发空的状态哦",
        BLOG_CATEGORY_NAME_IS_TOO_SHORT: u"博文分类名有点短呢",
        BLOG_TITLE_IS_TOO_SHORT: u"博文标题不能没有哦",
        BLOG_CONTENT_IS_TOO_SHORT: u"你知道卡拉赞毕业的基本要求是什么吗！那就是要在正文填写十五字！",
        BLOG_CATEGORY_NOT_FOUND: u"这个博文分类没有找到诶？好奇怪",
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

    def error_sql(self, se):
        return self.error(u'数据库出现错误，请检查输入')

    def error_unknown(self):
        msg = self.CODE_TO_MSG_MAP.get(self.UNKNOWN_ERROR)
        return self.error(msg)

logger = InoriLogger()
