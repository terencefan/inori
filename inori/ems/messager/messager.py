# -*- coding: utf-8 -*-

import logging

from .sendcloud import SendCloudMessager, SendCloudMessagerError

logger = logging.getLogger(__name__)

MessagerError = (
    SendCloudMessagerError,
)


class EMSMessagerError(Exception):
    pass


class EMSMessager(object):

    MESSAGER = {
        "sendcloud": SendCloudMessager,
    }

    NAME_TO_ID = {
        "sendcloud": 1,
    }

    ID_TO_NAME = {
        1: "send_cloud",
    }

    def __init__(self, messager, settings):
        logger.debug("EMSMessager Initializing ...")

        self.messagers = {}
        for name in self.MESSAGER:
            params = settings[name]
            try:
                self.messagers[name] = self.MESSAGER[name](**params)
            except MessagerError as me:
                raise EMSMessagerError(repr(me))

        self.set_messager(messager)

    def set_messager(self, messager):
        self.messager = self.messagers[messager]
        self.messager_id = self.NAME_TO_ID[messager]
        logger.info("messager set to: {}".format(messager))

    def send(self, sender, receiver, title, content):
        try:
            self.messager.send(sender, receiver, title, content)
            messager_id = self.messager_id
        except MessagerError as me:
            raise EMSMessagerError(repr(me))
        return messager_id
