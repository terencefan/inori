from flask import Flask
from inori.views.home import home
from inori.views.account import account

app = Flask(__name__)
app.register_module(home)
app.register_module(account, url_prefix='/admin')
