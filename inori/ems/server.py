# -*- coding: utf-8 -*-

"""
inori.ems.server
~~~~~~~~~~~~~~~~

This module provides a simple server for service serving.
"""

import logging

from inori.core.server import make_gevent_pool_server

from .sdk.ems import EmailService
from .dispatcher import EmailDispatcher

from .settings import EMS_THRIFT_SETTINGS

logger = logging.getLogger(__name__)


def server(host=None, port=None, pool_size=None, timeout=None):
    """
    EMS thrift server
    """
    host = host or EMS_THRIFT_SETTINGS["host"]
    port = port or EMS_THRIFT_SETTINGS["port"]
    pool_size = pool_size or EMS_THRIFT_SETTINGS["pool_size"]
    timeout = timeout or EMS_THRIFT_SETTINGS["timeout"]

    logger.info("making ems server at {0}:{1}".format(host, port))
    logger.info("pool size: {0}".format(pool_size))
    logger.info("timeout: {0}".format(timeout))

    return make_gevent_pool_server(
        EmailService, EmailDispatcher,
        host, port, pool_size, timeout,
    )
