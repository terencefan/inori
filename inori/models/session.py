# -*- coding:utf-8 -*-
from inori.settings import mysql_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**mysql_settings))
engine = create_engine(master_url,
                       pool_size=10,
                       max_overflow=-1,
                       pool_recycle=3600)
DBSession = sessionmaker(bind=engine)
