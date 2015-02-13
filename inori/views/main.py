# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    render_template_string,
)

from inori.settings import (
    INDEX_URLS,
    SOURCE_DIR,
)

bp = Blueprint('index', __name__)


def init_app(app):
    for url in INDEX_URLS:
        bp.add_url_rule(url, view_func=index)
    app.register_blueprint(bp)


def index(**kwargs):
    with open(SOURCE_DIR + '/static/modules/index/index.html') as f:
        return render_template_string(f.read().decode('utf-8'))
