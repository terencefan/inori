# -*- coding: utf-8 -*-

import datetime
import logging

from sqlalchemy.exc import SQLAlchemyError

from inori.ems.models import (
    DBSession,
    EmailSend,
)

from inori.ems.exc import (
    EMSErrorCode,
    raise_user_exc,
    raise_system_exc,
)

from . import messager

logger = logging.getLogger(__name__)


def process_send(email_id):
    session = DBSession()

    email_send = session.query(EmailSend).get(email_id)
    if not email_send:
        raise_user_exc(EMSErrorCode.EMAIL_SEND_NOT_FOUND)

    if email_send.status != EmailSend.STATUS_UNSEND:
        return

    sender_id = messager.send(email_send.sender,
                              email_send.receiver,
                              email_send.title,
                              email_send.content)
    if sender_id:
        email_send.messager_id = sender_id
        email_send.status = EmailSend.STATUS_SUCCESS
        email_send.send_at = datetime.datetime.now()
    else:
        email_send.status = EmailSend.STATUS_FAILED

    try:
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise_system_exc(EMSErrorCode.DATABASE_ERROR)
