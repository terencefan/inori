# -*- coding: utf-8 -*-

from inori.core.registry import ServiceRegistry
services = ServiceRegistry()

from . import settings
import logging.config
logging.config.dictConfig(settings.LOGGING)
