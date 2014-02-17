# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from inori.core.client import make_fake_client


def client(host=None, port=None, timeout=5, fake=True):
    if fake:
        return make_fake_client(
            "inori.ems.dispatcher:EmailDispatcher")
    else:
        return None
