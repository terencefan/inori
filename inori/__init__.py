from flask import Flask
from inori.views.home import home
from inori.views.account import account
from inori.views.wow import wow


inori = Flask(__name__)
inori.register_module(home)
inori.register_module(account, url_prefix='/account')
inori.register_module(wow, url_prefix='/wow')

redis_server = 'redis://:M06y05y1991@112.124.30.49'
