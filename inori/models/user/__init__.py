# -*- coding: utf-8 -*-

import hashlib

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

from inori.models import (
    Base,
    UIDBase,
)


class User(Base, UIDBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), default=u'')
    mobile = Column(BigInteger)
    password = Column(String(64), default=u'')
    nickname = Column(String(20), default=u'')
    is_super_admin = Column(Boolean, default=False)
    is_valid = Column(Boolean, default=False)
    created_at = Column(DateTime)
    welcome_info = Column(String(255), default=u'')

    def __init__(self, email, password=None, nickname=u''):
        self.email = email
        password = password or '123456'
        self.password = hashlib.sha256(password).hexdigest()
        self.nickname = nickname
        self.welcome_info = u"欢迎，{}".format(nickname)

    def authorize(self, password):
        return self.password == hashlib.sha256(password).hexdigest()
