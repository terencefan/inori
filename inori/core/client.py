# -*- coding: utf-8 -*-

import contextlib

dispatchers = {}


@contextlib.contextmanager
def make_fake_client(dispatcher):
    module, cls = dispatcher.split(':')
    yield _get_dispatcher(module, cls)


def _get_dispatcher(module, cls):
    global dispatchers
    if not module in dispatchers:
        dispatchers[module] = getattr(__import__(module, fromlist=module),
                                      cls)()
    return dispatchers[module]
