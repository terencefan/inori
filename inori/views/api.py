# -*- coding: utf-8 -*-

from flask import Blueprint

from inori.exc import InoriException

api = Blueprint('api', __name__)


def init_app(app):
    app.register_blueprint(api, url_prefix='/api')


@api.route('/ping')
def ping():
    return 'ok'


@api.errorhandler(InoriException)
def inori_error_handler(e):
    return e.message
