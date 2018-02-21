import os

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_from_flask():
    import pdb; pdb.set_trace()
    i = 3
    i = i + 1
    visited = i
    return "You have visited " + str(visited) + " times!!!"

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('port', 5000))
    app.debug = True
    app.run(host=host, port=port)
