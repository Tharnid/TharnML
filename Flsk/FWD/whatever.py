from flask import Flask
from flask import request
from flask import make_response
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hullo, from Flask!!!</h1>' + '<p>Your browser is {}</p><br />'.format(user_agent)
    # cookie monster
    response = make_response('<h1>This document carries cookies!!!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hullo, {}!!!</h1>'.format(name)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)
