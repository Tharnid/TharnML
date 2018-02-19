import os

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_from_flask():
    return 'Hello from a Flask World!'

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('port', 5000))
    app.debug = True
    app.run(host=host, port=port)
