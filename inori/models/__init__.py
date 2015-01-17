# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from inori.settings import MYSQL_SETTINGS

master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**MYSQL_SETTINGS))
engine = create_engine(
    master_url,
    convert_unicode=True,
    pool_size=10,
    max_overflow=-1,
    pool_recycle=3600,
)

DBSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = DBSession.query_property()

from .blog import Blog  # noqa
from .blog_category import BlogCategory  # noqa
from .tweet import Tweet  # noqa
