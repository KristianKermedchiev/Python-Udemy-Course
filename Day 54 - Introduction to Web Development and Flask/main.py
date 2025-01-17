from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/users/')
def users():
    return "This is the users page!"


if __name__ == '__main__':
    app.run()