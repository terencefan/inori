from flask import Flask
from inori.views.home import home

app = Flask(__name__)
app.register_module(home)
