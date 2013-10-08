# -*- coding:utf-8 -*-
import rsa


class RsaHelper():

    def __init__(self):

        with open('rsa.pub') as pubfile:
            p = pubfile.read()
            self.pubkey = rsa.PublicKey.load_pkcs1(p)

        with open('rsa.pri') as prifile:
            p = prifile.read()
            self.prikey = rsa.PrivateKey.load_pkcs1(p)

    def encrypt(self, message):
        return rsa.encrypt(message, self.pubkey)

    def decrypt(self, message):
        return rsa.decrypt(message, self.prikey)

if __name__ == '__main__':
    pubkey, prikey = rsa.newkeys(1024)

    pub = pubkey.save_pkcs1()
    pubfile = open('rsa.pub', 'w+')
    pubfile.write(pub)
    pubfile.close()

    pri = prikey.save_pkcs1()
    prifile = open('rsa.pri', 'w+')
    prifile.write(pri)
    prifile.close()

rsa_helper = RsaHelper()
