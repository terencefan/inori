# -*- coding: utf-8 -*-

"""
zeus.core.server
~~~~~~~~~~~~~~~~

This module provides a general make_server function.
"""

import logging
import multiprocessing
import signal
import time

import gevent
import gevent.pool

from ctypes import c_int

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

TSocket.socket = gevent.socket


logger = logging.getLogger(__name__)


def timeout_handler(signum, frame):
    raise TServerTimeout


class TServerTimeout(Exception):
    pass


class TProcessPoolServer(TServer.TServer):
    """
    Refine TProcessPoolServer with more functions.

    1. support process timeout. will kill server process when timeout reached.
    2. can get active process count by active_count property.
    """
    def __init__(self, *args, **kwargs):
        TServer.TServer.__init__(self, *args)

        self._counter_lock = multiprocessing.Lock()
        self._active_count = multiprocessing.Value(c_int, 0)

        self.pool_size = kwargs.get('pool_size', 10)
        self.timeout = kwargs.get('timeout', 30)
        self.workers = []

    def _handle(self):
        signal.signal(signal.SIGALRM, timeout_handler)

        while True:
            try:
                client = self.serverTransport.accept()
                self._serve_client(client)
            except (SystemExit, KeyboardInterrupt):
                break
            except Exception as x:
                logging.exception(x)

    def _serve_client(self, client):
        with self._counter_lock:
            self._active_count.value += 1

        try:
            signal.alarm(self.timeout)
            itrans = self.inputTransportFactory.getTransport(client)
            otrans = self.outputTransportFactory.getTransport(client)
            iprot = self.inputProtocolFactory.getProtocol(itrans)
            oprot = self.outputProtocolFactory.getProtocol(otrans)

            try:
                while True:
                    self.processor.process(iprot, oprot)
            except TTransport.TTransportException:
                pass
            except TServerTimeout:
                logging.error("Timed out!")
        finally:
            itrans.close()
            otrans.close()
            signal.alarm(0)

        with self._counter_lock:
            self._active_count.value -= 1

    @property
    def active_count(self):
        return self._active_count.value

    def serve(self):
        self.serverTransport.listen()

        for i in range(self.pool_size):
            p = multiprocessing.Process(target=self._handle)
            p.daemon = True
            p.start()
            self.workers.append(p)

        while True:
            try:
                if self._active_count.value >= self.pool_size * 0.8:
                    logging.warning(
                        "Currently using %d workers, pool seems busy, "
                        "you may need to increase pool size!" %
                        self._active_count.value)
                time.sleep(1)

            except (SystemExit, KeyboardInterrupt):
                break

            except Exception as e:
                logging.exception(e)


class TGeventServer(TServer.TServer):
    def __init__(self, *args, **kwargs):
        TServer.TServer.__init__(self, *args)
        self.timeout = kwargs.get('timeout', 30)

    def serve(self):
        self.serverTransport.listen()

        while True:
            try:
                client = self.serverTransport.accept()
                gevent.spawn(self._serve_client, client)
            except (SystemExit, KeyboardInterrupt):
                break
            except Exception as x:
                logging.exception(x)

    def _serve_client(self, client):
        try:
            itrans = self.inputTransportFactory.getTransport(client)
            otrans = self.outputTransportFactory.getTransport(client)
            iprot = self.inputProtocolFactory.getProtocol(itrans)
            oprot = self.outputProtocolFactory.getProtocol(otrans)

            try:
                while True:
                    with gevent.Timeout(self.timeout, TServerTimeout):
                        self.processor.process(iprot, oprot)
            except TTransport.TTransportException:
                pass
        except TServerTimeout:
            logging.error("Timed out!")
        finally:
            itrans.close()
            otrans.close()


class TGeventPoolServer(TServer.TServer):
    def __init__(self, *args, **kwargs):
        TServer.TServer.__init__(self, *args)

        self.pool_size = kwargs.get('pool_size', 10)
        self.timeout = kwargs.get('timeout', 30)
        self.workers = []

    def _handle(self):
        while True:
            try:
                client = self.serverTransport.accept()
                gevent.spawn(self._serve_client, client)
            except (SystemExit, KeyboardInterrupt):
                break
            except Exception as x:
                logging.exception(x)

    def _serve_client(self, client):
        try:
            itrans = self.inputTransportFactory.getTransport(client)
            otrans = self.outputTransportFactory.getTransport(client)
            iprot = self.inputProtocolFactory.getProtocol(itrans)
            oprot = self.outputProtocolFactory.getProtocol(otrans)

            try:
                while True:
                    with gevent.Timeout(self.timeout, TServerTimeout):
                        self.processor.process(iprot, oprot)
            except TTransport.TTransportException:
                pass
        except TServerTimeout:
            logging.error("Timed out!")
        finally:
            itrans.close()
            otrans.close()

    def serve(self):
        self.serverTransport.listen()

        for i in range(self.pool_size):
            p = multiprocessing.Process(target=self._handle)
            p.daemon = True
            p.start()
            self.workers.append(p)

        for p in self.workers:
            p.join()


def make_gevent_pool_server(
        service, dispatcher, host, port, pool_size=10, timeout=30):
    processor = service.Processor(dispatcher())
    transport = TSocket.TServerSocket(host=host, port=port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolAcceleratedFactory()

    server = TGeventPoolServer(processor, transport, tfactory, pfactory,
                               pool_size=pool_size, timeout=timeout)
    return server


def make_gevent_server(service, dispatcher, host, port, timeout=30):
    processor = service.Processor(dispatcher())
    transport = TSocket.TServerSocket(host=host, port=port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolAcceleratedFactory()

    server = TGeventServer(processor, transport, tfactory, pfactory,
                           timeout=timeout)
    return server
