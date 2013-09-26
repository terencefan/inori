from flask import Flask
app = Flask(__name__)

from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
