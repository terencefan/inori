# -*- coding: utf-8 -*-

import inspect
import logging

logger = logging.getLogger(__name__)

from inori.core.client import make_client, make_fake_client
from .settings import EMS_THRIFT_SETTINGS

from .sdk.ems import EmailService
from .sdk.ems import constants


def client(host=None, port=None, timeout=5, fake=True):
    if fake:
        return make_fake_client(
            "inori.ems.dispatcher:EmailDispatcher")
    else:
        host = host or EMS_THRIFT_SETTINGS['host']
        port = port or EMS_THRIFT_SETTINGS['port']
        return make_client(EmailService, host, port, timeout)


client.apis = [i[0] for i in inspect.getmembers(EmailService.Iface,
                                                predicate=inspect.ismethod)]
client.constants = constants
client.error = (constants.EMSUserException,
                constants.EMSSystemException,
                constants.EMSUnknownException)
client.error_code = constants.EMSErrorCode
