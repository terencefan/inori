# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    SmallInteger,
    String,
    Text,
)

from .database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    password = Column(String(20), default=u"123456")
    nickname = Column(String(20), default=u"")
    is_super_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    welcome_info = Column(String(200), default=u"")
    created_at = Column(DateTime)
    last_login_time = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.welcome_info = u"欢迎，{}".format(nickname)

    def authorize(self, password):
        return self.password == password


class EmailSend(Base):
    __tablename__ = 'email_send'

    STATUS_NOT_SEND = 0
    STATUS_SUCCESS = 1
    STATUS_WAITING = 2
    STATUS_FAILED = -1

    id = Column(Integer, primary_key=True)
    to_email = Column(String(30), default=u"")
    title = Column(String(50), default=u"")
    content = Column(Text, default=u"")
    status = Column(SmallInteger, default=0)
    retry_times = Column(SmallInteger, default=0)
    created_at = Column(DateTime)

    def __init__(self, to_email, title, content):
        self.to_email = to_email
        self.title = title
        self.content = content
