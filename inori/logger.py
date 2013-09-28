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
    REPEAT_PWD_MISMATCH = 701
    TWEET_IS_TOO_SHORT = 702
    BLOG_CATEGORY_NAME_IS_TOO_SHORT = 703
    BLOG_TITLE_IS_TOO_SHORT = 704
    BLOG_CONTENT_IS_TOO_SHORT = 705
    BLOG_CATEGORY_NOT_FOUND = 706

    CODE_TO_MSG_MAP = {
        UNKNOWN_ERROR: u"一些奇怪的错误粗线了！",
        PERMISSION_DENIED: u"噗噗噗，这可不是你能来的地方",

        USER_AUTH_FAILED: u"看起来就是输错邮箱或密码了，一股弱者的气息",
        REPEAT_PWD_MISMATCH: u'不好好确认密码的话就不给你注册！',
        TWEET_IS_TOO_SHORT: u"是不可以发空的状态哦",
        BLOG_CATEGORY_NAME_IS_TOO_SHORT: u"博文分类名有点短呢",
        BLOG_TITLE_IS_TOO_SHORT: u"博文标题不能没有哦",
        BLOG_CONTENT_IS_TOO_SHORT: u"你知道卡拉赞毕业的基本要求是什么吗！那就是要在正文填写十五字！",
        BLOG_CATEGORY_NOT_FOUND: u"这个博文分类没有找到诶？好奇怪",
    }

    KEY_TO_MSG_MAP = {
        'email': u"这货不是邮箱！这货不是邮箱！",
        'password': u"警告！警告！需要一个8-15位的字母数字组合才能通行",
    }

    def info(self, msg):
        init_session()
        session['info_list'].append(msg)

    def info_code(self, code):
        msg = ""
        return self.info(msg)

    def error(self, msg):
        init_session()
        session['error_list'].append(msg)

    def error_code(self, code):
        msg = self.CODE_TO_MSG_MAP.get(code, u"一些奇怪的错误粗线了！")
        return self.error(msg)

    def error_format(self, key):
        msg = self.KEY_TO_MSG_MAP.get(key, u"`{}`格式错误".format(key))
        return self.error(msg)

    def error_sql(self, se):
        return self.error(u'数据库出现错误，请检查输入')

    def error_unknown(self):
        msg = self.CODE_TO_MSG_MAP.get(self.UNKNOWN_ERROR)
        return self.error(msg)

logger = InoriLogger()
