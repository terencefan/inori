# -*- coding: utf-8 -*-

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
)

from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    password = Column(String(20), default=u"123456")
    nickname = Column(String(20), default=u"")
    is_super_admin = Column(Boolean, default=False)
    welcome_info = Column(String(200), default=u"")

    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.welcome_info = u"欢迎，{}".format(nickname)
