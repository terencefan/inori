# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
)


###############
# Table Declare
###############

from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()


class EmailSend(DeclarativeBase):
    __tablename__ = 'email_send'

    id = Column(Integer, primary_key=True)
    sender = Column(String(32), default=u"")
    receiver = Column(String(32), default=u"")
    title = Column(String(255), default=u"")
    content = Column(Text, default=u"")
    created_at = Column(DateTime)
    send_at = Column(DateTime)
