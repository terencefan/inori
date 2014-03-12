# -*- coding: utf-8 -*-

ENV = "dev"

SERVICES = [
    "inori.ems",
]

MYSQL_SETTINGS = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "19910720",
    "database": "inori",
}

###############
# EMS SETTINGS
###############

EMS_MYSQL_SETTINGS = MYSQL_SETTINGS

EMS_MESSAGER = "sendcloud"
EMS_MESSAGER_SETTINGS = {
    "sendcloud": {
        "host": "https://sendcloud.sohu.com/webapi/",
        "api_user": "postmaster@stdrickforce.sendcloud.org",
        "api_key": "n4RyDFEi",
    }
}
