from flask import Flask
app = Flask(__name__)

from flask import render_template

from models import (
    DBSession,
    Tweet,
)


@app.route('/')
@app.route('/index')
def index():
    session = DBSession()
    tweets = session.query(Tweet).\
        filter(Tweet.user_id == 1).\
        order_by(Tweet.created_at.desc())

    var = {
        'tweets': tweets,
    }
    return render_template('index.html', var=var)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
