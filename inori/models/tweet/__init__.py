# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
)

from .database import Base


class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    content = Column(String(200), default=u"")
    created_at = Column(DateTime)

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content
