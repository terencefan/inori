# -*- coding: utf-8 -*-

from .category import BlogCategory

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
)

from inori.models import (
    Base,
    UIDBase,
)


class Blog(Base, UIDBase):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    category_id = Column(Integer, default=0)
    title = Column(String(50), default=u"")
    content = Column(Text, default=u"")
    created_at = Column(DateTime)

    def __init__(self, user_id, title, content=u""):
        self.user_id = user_id
        self.title = title
        self.content = content

    @property
    def category_name(self):
        category = BlogCategory.get(self.category_id)
        return category.name if category else u'没有分类呢'
