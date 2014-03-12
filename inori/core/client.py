# -*- coding: utf-8 -*-

import contextlib

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

dispatchers = {}


@contextlib.contextmanager
def make_client(service, host, port, timeout=3):
    try:
        transport = TSocket.TSocket(host, port)
        transport.setTimeout(timeout * 1000)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocolAccelerated(transport)
        transport.open()
        yield service.Client(protocol)
    finally:
        transport.close()


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
