# -*- coding: utf-8 -*-

import requests


class SendCloudMessagerError(Exception):
    pass


class SendCloudMessager(object):

    def __init__(self, host, api_user, api_key):
        self.NAME = u"SendCloud"

        self.host = host
        self.api_user = api_user
        self.api_key = api_key

        self.params = {
            'api_user': self.api_user,
            'api_key': self.api_key,
        }

    def send(self, sender, receiver, title, content):

        params = dict(self.params)
        params.update({
            'from': sender,
            'to': receiver,
            'subject': title,
            'html': content,
        })

        try:
            r = requests.post("{}{}".format(self.host, "mail.send.xml"),
                              data=params, timeout=10)
        except Exception as e:
            raise SendCloudMessagerError(e)
