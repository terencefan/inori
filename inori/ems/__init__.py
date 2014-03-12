# -*- coding: utf-8 -*-

import logging

from .client import client

from .models import DBSession

from .sdk.ems.constants import (
    EMSUserException,
    EMSSystemException,
    EMSUnknownException,
    EMSErrorCode,
)

from inori.core.service import Service

NAME = "inori.ems"
EMSError = (
    EMSUserException,
    EMSSystemException,
    EMSUnknownException,
)


def main():

    return Service(
        name=NAME,
        slug=NAME.split('.')[:-1],
        client=client,
        timeout=3*1000,

        logger=logging.getLogger(NAME),

        dbsession=DBSession,

        user_exc=EMSUserException,
        system_exc=EMSSystemException,
        unknown_exc=EMSUnknownException,

        error=EMSError,
        error_code=EMSErrorCode,
    )
