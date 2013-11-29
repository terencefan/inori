# -*- coding: utf-8 -*-
from flask import flash

"""
inori.logger
============

This module contains all Exception
"""


class InoriLogger(object):

    # SYSTEM_ERROR
    UNKNOWN_ERROR = 600
    PERMISSION_DENIED = 601

    # USER_EXCEPTION
    USER_NOT_FOUND = 700
    USER_AUTH_FAILED = 701
    TWEET_IS_TOO_SHORT = 702
    BLOG_CATEGORY_NAME_IS_TOO_SHORT = 703
    BLOG_TITLE_IS_TOO_SHORT = 704
    BLOG_CONTENT_IS_TOO_SHORT = 705
    BLOG_CATEGORY_NOT_FOUND = 706
    REPEAT_PWD_MISMATCH = 707

    CODE_TO_MSG_MAP = {
        UNKNOWN_ERROR: u"一些奇怪的错误粗线了！",
        PERMISSION_DENIED: u"您无权访问此链接，如有疑问请联系小祈哦~",
        USER_NOT_FOUND: u"你确定这么个人存在嘛？啊？",
        USER_AUTH_FAILED: u"一看就是输错密码了，充满着弱者的气息",
        TWEET_IS_TOO_SHORT: u"是不可以发空的状态哦",
        BLOG_CATEGORY_NAME_IS_TOO_SHORT: u"博文分类名有点短呢",
        BLOG_TITLE_IS_TOO_SHORT: u"博文标题不能没有哦",
        BLOG_CONTENT_IS_TOO_SHORT: u"你知道卡拉赞毕业的基本要求是什么吗！那就是要在正文填写十五字！",
        BLOG_CATEGORY_NOT_FOUND: u"这个博文分类没有找到诶？好奇怪",
        REPEAT_PWD_MISMATCH: u'不好好确认密码的话就不给你注册！',
    }

    KEY_TO_MSG_MAP = {
        'email': u"这货不是邮箱！这货不是邮箱！",
        'password': u"警告！警告！需要一个8-15位的字母数字组合才能通行",
    }

    def info(self, msg):
        flash(msg, 'info')

    def info_code(self, code):
        msg = ""
        return self.info(msg)

    def error(self, msg):
        flash(msg, 'error')

    def error_code(self, code):
        msg = self.CODE_TO_MSG_MAP.get(code, u"一些奇怪的错误粗线了！")
        return self.error(msg)

    def error_format(self, key):
        msg = self.KEY_TO_MSG_MAP.get(key, u"`{}`格式错误".format(key))
        return self.error(msg)

    def error_sql(self, se):
        print se
        return self.error(u'数据库出现错误，请检查输入')

    def error_unknown(self):
        msg = self.CODE_TO_MSG_MAP.get(self.UNKNOWN_ERROR)
        return self.error(msg)

logger = InoriLogger()
