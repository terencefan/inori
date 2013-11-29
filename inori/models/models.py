# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    String,
    Text,
)

from .database import Base


class KeyString(Base):
    __tablename__ = 'key_string'

    key = Column(String(50), primary_key=True)
    value = Column(Text, default=u'')
