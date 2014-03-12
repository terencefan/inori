# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from inori.ems.settings import EMS_MYSQL_SETTINGS


###############
# Session Maker
###############
master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**EMS_MYSQL_SETTINGS))
engine = create_engine(master_url,
                       convert_unicode=True,
                       pool_size=10,
                       max_overflow=-1,
                       pool_recycle=3600)

DBSession = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))


###############
# Table Declare
###############

DeclarativeBase = declarative_base()


class EmailSend(DeclarativeBase):
    __tablename__ = 'email_send'

    STATUS_UNSEND = 0
    STATUS_SUCCESS = 1
    STATUS_FAILED = 2

    id = Column(Integer, primary_key=True)
    sender = Column(String(32), default=u"")
    receiver = Column(String(32), default=u"")
    title = Column(String(255), default=u"")
    content = Column(Text, default=u"")
    status = Column(Integer, default=0)
    created_at = Column(DateTime)
    send_at = Column(DateTime)


def init_db():
    DeclarativeBase.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
