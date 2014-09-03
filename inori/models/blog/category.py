# -*- coding: utf-8 -*-

from sqlalchemy import (
    Column,
    Integer,
    String,
)

from inori.models import (
    Base,
    UIDBase,
)


class BlogCategory(Base, UIDBase):
    __tablename__ = 'blog_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), default=u"")

    def __init__(self, name):
        self.name = name
