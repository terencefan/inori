#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def server():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="ems/sms etc.")
    args = parser.parse_args()

    service_server = __import__("inori.{}.server".format(args.name),
                                fromlist="{}.server".format(args.name))
    getattr(service_server, "server")().serve()


def helper():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="ems/sms etc.")
    parser.add_argument("-r", "--real", action="store_true",
                        help="force use real client")
    args = parser.parse_args()

    fake = args.real is not True
    service_client = __import__("inori.{}.client".format(args.name),
                                fromlist="{}.client".format(args.name))

    with getattr(service_client, "client")(timeout=30 * 1000, fake=fake) as c:
        c.ping()
        import IPython
        IPython.embed()
