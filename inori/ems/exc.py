# -*- coding: utf-8 -*-

"""
inori.ems.exceptions
~~~~~~~~~~~~~~~~~~~~

This module contains all error_code and raise_exception function in ems.
"""

from .sdk.ems.ttypes import (
    EMSErrorCode,
    EMSUserException,
    EMSSystemException,
)

TRANSLATIONS = {
    EMSErrorCode.SEND_TIMEOUT: u"email发送超时",
}


def raise_user_exc(error_code):
    """
    Raise UserException which error message shall be shown to user.

    :param error_code: Error code defined in thrift.
    """
    raise EMSUserException(
        error_code,
        EMSErrorCode._VALUES_TO_NAMES[error_code],
        TRANSLATIONS[error_code],
    )


def raise_system_exc(error_code):
    """
    Raise UserException which error message shall be shown to user.

    :param error_code: Error code defined in thrift.
    """
    raise EMSSystemException(
        error_code,
        EMSErrorCode._VALUES_TO_NAMES[error_code],
        TRANSLATIONS[error_code],
    )
