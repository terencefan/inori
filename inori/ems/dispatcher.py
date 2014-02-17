# -*- coding: utf-8 -*-

"""
zeus.ems.dispatcher
~~~~~~~~~~~~~~~~~~~

The main ems server api controller.

Distribute requests to different handlers and serialize object to thrift struct
when needed.
"""

import logging

from .handler import (
    base,
    inner,
)

from inori.core.decorators import (
    dispatcher,
)

logger = logging.getLogger(__name__)


@dispatcher
class EmailDispatcher(object):
    def __init__(self):
        logger.info("ems server starting..")

    #####
    # Base APIs
    #####

    def ping(self):
        return base.ping()

    def send(self, sender, receiver, title, content):
        return base.send(sender, receiver, title, content)

    def set_messager(self, name):
        return base.set_messager(name)

    #####
    # Inner APIs
    #####

    def process_send(self, email_id):
        return inner.process_send(email_id)
