# -*- coding: utf-8 -*-

from inori.settings import SERVICES

UNREGISTERED_FMT = """
    Service %s is not registered.
"""

class NotRegistered(KeyError):
    def __repr__(self):
        return UNREGISTERED_FMT.format(self)


class ServiceRegistry(dict):
    NotRegistered = NotRegistered

    def __init__(self, *args, **kwargs):
        super(ServiceRegistry, self).__init__(*args, **kwargs)

        self._services = {}
        for name in SERVICES:
            main = getattr(__import__(name, fromlist=name), "main")
            self._services[name] = main

    def __getitem__(self, key):
        if key not in self._services:
            raise NotRegistered(key)

        if callable(self._services[key]):
            self._services[key] = self._services[key]()
        return self._services[key]

    def __iter__(self):
        return iter(self._services)

    def __contains__(self, key):
        return key in self._services
