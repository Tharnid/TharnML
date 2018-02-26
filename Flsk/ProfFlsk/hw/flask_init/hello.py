import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bloody Index Page!!!"

@app.route('/user/<username>')
def show_user(username):
    # show the user profile
    return "User " + str(username)

@app.route('/hello')
def hello_from_flask():
    return "Hello!!!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show post with given id..id must be int
    return "Post %d" % post_id # str(post_id)



if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('port', 5000))
    app.debug = True
    app.run(host=host, port=port)
