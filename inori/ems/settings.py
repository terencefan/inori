# -*- coding: utf-8 -*-

EMS_THRIFT_SETTINGS = {
    "host": "0.0.0.0",
    "port": 19090,
    "pool_size": 1,
    "timeout": 30,
}

EMS_MYSQL_SETTINGS = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "",
    "database": "sms",
}

EMS_MESSAGER = ""

EMS_MESSAGER_SETTINGS = {
    "sendcloud": {
        "host": "https://sendcloud.sohu.com/webapi/",
        "api_user": "",
        "api_key": "",
    }
}

from inori.settings import *
