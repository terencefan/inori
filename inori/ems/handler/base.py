# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from inori.ems.models import (
    EmailSend,
)

from . import messager


def ping():
    return True


def send(sender, receiver, title, content):
    email = EmailSend(
        sender=sender,
        receiver=receiver,
        title=title,
        content=content,
    )
    return process_send(email)


def set_messager(name):
    messager.set_messager(name)


def process_send(email):
    messager.send(
        email.sender, email.receiver, email.title, email.content)
