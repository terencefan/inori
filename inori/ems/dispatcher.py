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
