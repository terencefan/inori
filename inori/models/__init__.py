# -*- coding:utf-8 -*-

from inori.settings import mysql_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**mysql_settings))
engine = create_engine(
    master_url,
    convert_unicode=True,
    pool_size=10,
    max_overflow=-1,
    pool_recycle=3600
)

DBSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = DBSession.query_property()


class UIDBase(object):

    @classmethod
    def get(clazz, uid):
        return DBSession().query(clazz).get(uid)

    @classmethod
    def mget(clazz, uids):
        return DBSession().query(clazz).filter(clazz.id.in_(uids))


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)


from user import (
    User,
)

from blog import (
    Blog,
    BlogCategory,
)

from tweet import (
    Tweet,
)
