# -*- coding:utf-8 -*-
import distutils.sysconfig
import os

site_path = distutils.sysconfig.get_python_lib()

f = open("{}/inori.pth".format(site_path), 'w')
f.write(os.getcwd())
f.close()

from inori import app

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "_g\x13`\x03\xd8rMg\x1a\x04i6\xbeuV'\xa1\r]\xbf\xa7\xf0N"
    app.run(host='0.0.0.0')
