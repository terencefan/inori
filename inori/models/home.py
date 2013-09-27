# -*- coding: utf-8 -*-

from inori.settings import mysql_settings

from sqlalchemy import create_engine
master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**mysql_settings))
engine = create_engine(master_url)

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()

from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)


class User(DeclarativeBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(30))
    password = Column(String(20), default=u"123456")
    nickname = Column(String(20), default=u"")
    is_super_admin = Column(Boolean, default=False)

    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname


class Tweet(DeclarativeBase):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    content = Column(String(200), default=u"")
    created_at = Column(DateTime)

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


if __name__ == '__main__':
    DeclarativeBase.metadata.create_all(engine)
