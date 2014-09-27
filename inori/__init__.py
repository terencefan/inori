from flask import Flask
from inori.views.home import home
from inori.views.account import account
from inori.views.wow import wow


class MyFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update({
        'variable_start_string': '{{ ',
        'variable_end_string': ' }}',
    })

inori = MyFlask(__name__)
inori.register_module(home)
inori.register_module(account, url_prefix='/account')
inori.register_module(wow, url_prefix='/wow')

redis_server = 'redis://:M06y05y1991@112.124.30.49'
