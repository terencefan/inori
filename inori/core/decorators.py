# -*- coding: utf-8 -*-

import functools
import inspect
import logging
import time

from thrift.Thrift import TException

from inori import services

_extra_service_name = lambda x: '.'.join(x.split('.')[:2])


def dispatcher(cls):
    def _decorate(func, service):
        @functools.wraps(func)
        def wrapper(self, *args):
            time_start = time.time()
            try:
                return func(self, *args)

            except TException as te:
                msg = u"{0} => {1}{2}".format(te.message, func.func_name, args)
                if isinstance(te, service.user_esc):
                    logger.warning(msg)
                else:
                    logger.exception(msg)
                raise

            except Exception as e:
                logger.exception("{0} => {1}{2}".format(
                    e, func.func_name, args))
                raise service.unknown_exc(
                    service.error_code.UNKNOWN_ERROR,
                    service.error_code._VALUES_TO_NAMES[
                        service.error_code.UNKNOWN_ERROR],
                    repr(e),
                )
            finally:
                real_time = (time.time() - time_start) * 1000

                if real_time >= service.timeout:
                    logger.warning("Time out! {0}{1} => {2}ms".format(
                        func.func_name, args, real_time))
                else:
                    logger.info("{0}{1} response time {2}ms".format(
                        func.func_name, args, real_time))

        return wrapper

    logger = logging.getLogger(cls.__module__)
    service_name = _extra_service_name(cls.__module__)
    service = services[service_name]
    for name, method in inspect.getmembers(cls, inspect.ismethod):
        setattr(cls, name, _decorate(method, service))

    return cls
