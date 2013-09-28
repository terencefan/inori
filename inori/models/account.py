# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
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
