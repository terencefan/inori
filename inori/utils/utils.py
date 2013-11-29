# -*- coding: utf-8 -*-
import base64
import json
import rsa

from flask import (
    redirect,
    request,
    session,
    url_for,
)

from sqlalchemy.exc import SQLAlchemyError

from inori.logger import logger
from inori.models import (
    dbsession,
    EmailSend,
    KeyString,
)


class RsaHelper():

    def __init__(self):

        rsa_pub = dbsession.query(KeyString).\
            get('rsa_pub').value
        rsa_pri = dbsession.query(KeyString).\
            get('rsa_pri').value

        self.pubkey = rsa.PublicKey.load_pkcs1(rsa_pub)
        self.prikey = rsa.PrivateKey.load_pkcs1(rsa_pri)

    def encrypt(self, message):
        return rsa.encrypt(message, self.pubkey)

    def decrypt(self, message):
        return rsa.decrypt(message, self.prikey)


def dbcommit():
    try:
        dbsession.commit()
    except SQLAlchemyError as se:
        logger.error_sql(se)
        return redirect_back()


def redirect_back():
    if request.referrer:
        return redirect(request.referrer)
    else:
        return redirect(url_for('home.index'))


def send_email(to_email, title, content):
    email_send = EmailSend(to_email, title, content)
    dbsession.add(email_send)

    try:
        dbsession.commit()
        return True
    except:
        return False


def set_user(user):

    session['logged_in'] = True
    session['user'] = {
        'id': user.id,
        'email': user.email,
        'nickname': user.nickname,
        'is_super_admin': user.is_super_admin,
        'is_active': user.is_active,
    }


def pack_params(**kwargs):
    params = {}
    for key, val in kwargs.items():
        params[key] = val

    rsa_helper = RsaHelper()
    message = json.dumps(params)
    message = rsa_helper.encrypt(message)
    return base64.encodestring(message)


def unpack_params(message):
    rsa_helper = RsaHelper()
    message = base64.decodestring(message)
    message = rsa_helper.decrypt(message)
    return json.loads(message)


if __name__ == '__main__':
    pubkey, prikey = rsa.newkeys(1024)

    pub = pubkey.save_pkcs1()
    rsa_pub = dbsession.query(KeyString).get('rsa_pub')
    if not rsa_pub:
        rsa_pub = KeyString(key='rsa_pub')
        dbsession.add(rsa_pub)
    rsa_pub.value = pub

    pri = prikey.save_pkcs1()
    rsa_pri = dbsession.query(KeyString).get('rsa_pri')
    if not rsa_pri:
        rsa_pri = KeyString(key='rsa_pri')
        dbsession.add(rsa_pri)
    rsa_pri.value = pri

    dbsession.commit()
