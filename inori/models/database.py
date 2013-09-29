# -*- coding:utf-8 -*-
from inori.settings import mysql_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**mysql_settings))
engine = create_engine(master_url,
                       convert_unicode=True,
                       pool_size=10,
                       max_overflow=-1,
                       pool_recycle=3600)

dbsession = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = dbsession.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
