from celery import Celery
from flask import Flask
from inori.views.home import home
from inori.views.account import account


inori = Flask(__name__)
inori.register_module(home)
inori.register_module(account, url_prefix='/account')

redis_server = 'redis://:M06y05y1991@112.124.30.49'
celery = Celery('inori', backend=redis_server, broker=redis_server)


@celery.task
def add(x, y):
    return x + y
