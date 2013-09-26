# -*- coding: utf-8 -*-

from settings import mysql_settings

from sqlalchemy import create_engine
master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**mysql_settings))
engine = create_engine(master_url)

from sqlalchemy import (
    Boolean,
    Column,
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


if __name__ == '__main__':
    # DeclarativeBase.metadata.create_all(engine)
    q = DBSession().query(User).get(1)
    print q
