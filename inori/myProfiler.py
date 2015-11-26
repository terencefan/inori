#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

import cProfile


class Profiler(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.run_profile(environ, start_response)

    def run_profile(self, environ, start_response):
        prof = cProfile.Profile()
        response_body = []

        def catching_start_response(status, headers, exc_info=None):
            start_response(status, headers, exc_info)
            return response_body.append

        def runapp():
            appiter = self.app(environ, catching_start_response)
            try:
                response_body.extend(appiter)
            finally:
                if hasattr(appiter, 'close'):
                    appiter.close()

        prof.runcall(runapp)
        body = b''.join(response_body)
        results = prof.getstats()

        with open('/data/shequ_x1/prof', 'a') as f:
            f.write(str(results))

        return [body]
