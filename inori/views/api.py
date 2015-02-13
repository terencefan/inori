# -*- coding: utf-8 -*-

from flask import Blueprint

from inori.exc import InoriException

bp = Blueprint('api', __name__)


def init_app(app):
    app.register_blueprint(bp, url_prefix='/api')


@bp.errorhandler(InoriException)
def inori_error_handler(e):
    return e.message
