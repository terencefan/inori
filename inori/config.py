#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Fri Aug 21 18:18:45 2015
# Updated At: Tue Sep 15 14:52:01 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import os

PROJECT = 'inori'

#: dev, prodb, prod
ENV = os.getenv('ENV', 'prod')
DEBUG = True
SECRET_KEY = '01b9dcc46e2b4d3890b992dbafcd8ecd'

STATIC_DIR = '/'.join(os.path.dirname(__file__).split('/')[:-1] + ['static'])
# if ENV == 'prod':
#     STATIC_DIR = '/srv/inori/static'

#: default redis dsn
REDIS_DSN = 'redis://localhost:6379'

MONGO_SETTINGS = {
    'db': 'inori',
    'host': '52.69.235.67',
    'port': 27017,
}

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
