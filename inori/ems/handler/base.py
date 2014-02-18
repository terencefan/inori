# -*- coding: utf-8 -*-

import logging

from sqlalchemy.exc import SQLAlchemyError

from inori.ems.models import (
    DBSession,
    EmailSend,
)

from inori.ems.exc import (
    EMSErrorCode,
    raise_system_exc,
)

from . import messager

logger = logging.getLogger(__name__)


def ping():
    return True


def send(sender, receiver, title, content):
    session = DBSession()

    email_send = EmailSend(
        sender=sender,
        receiver=receiver,
        title=title,
        content=content,
    )
    session.add(email_send)

    session.flush()
    # print email_send.id

    try:
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise_system_exc(EMSErrorCode.DATABASE_ERROR, repr(e))


def set_messager(name):
    messager.set_messager(name)
