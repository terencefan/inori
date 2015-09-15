#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Fri Aug 21 18:18:45 2015
# Updated At: Tue Sep 15 13:55:35 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from os.path import (
    abspath,
    split,
)

PROJECT = 'inori'

#: dev, prodb, prod
ENV = 'dev'
DEBUG = True
SECRET_KEY = '01b9dcc46e2b4d3890b992dbafcd8ecd'

STATIC_DIR = abspath(split(__file__)[0])[:-len(PROJECT)] + 'static/build'
print 'static_dir: %s' % STATIC_DIR

#: default mongodb dsn
MONGODB_DSN = 'mongodb://localhost:27017/inori_dev'

#: default redis dsn
REDIS_DSN = 'redis://localhost:6379'

#: default celery broker
CELERY_BROKER = 'amqp://admin:admin@localhost:5672/inori'

#: default log settings
LOGGING_SETTINGS = {
    'version': 1,

    'disable_existing_loggers': False,

    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },

    'loggers': {
        'inori': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        }
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'general',
        },
    },

    'formatters': {
        'general': {
            'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                      ' %(message)s'
        },
    }
}
