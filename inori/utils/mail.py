# -*- coding: utf-8 -*-

import requests

from sqlalchemy.exc import SQLAlchemyError

from xml.etree import ElementTree

from inori.settings import email_settings

from inori.models import (
    dbsession,
    EmailSend,
)


def send_mail(to_email, title, content):

    email_send = EmailSend(to_email, title, content)

    url = "https://sendcloud.sohu.com/webapi/mail.send.xml"
    sendcloud = email_settings['sendcloud']
    params = {
        'api_user': sendcloud['api_user'],
        'api_key': sendcloud['api_key'],
        'from': 'stdrickforce@gmail.com',
        'to': to_email,
        'fromname': u'小祈和小翼的储藏室',
        'subject': title,
        'html': content,
    }
    r = requests.post(url, data=params)
    xml = ElementTree.fromstring(r.text)
    message = xml.find('message').text

    if message == 'success':
        email_send.status = EmailSend.STATUS_SUCCESS
    elif message == 'error':
        email_send.status = EmailSend.STATUS_FAILED
        errors = xml.find('errors')
        errors = errors.findall('error')
        email_send.remark = ';'.join([error.text for error in errors])
    else:
        email_send.status = EmailSend.STATUS_UNKNOWN
        email_send.remark = message

    dbsession.add(email_send)
    try:
        dbsession.commit()
        return True
    except SQLAlchemyError:
        return False


if __name__ == '__main__':
    send_mail('tengyuan.fan@ele.me', u'测试', u'对二氯苯×反氯化苯')
