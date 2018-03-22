import os
import pymysql

from flask import Flask, request, render_template, redirect, url_for, flash, session
app = Flask(__name__)

import logging
from logging.handlers import RotatingFileHandler

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully Logged In!!!")
            # return redirect(url_for('welcome', username=request.form.get('username'))
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username and/or password'
            app.logger.warning('Incorrect username and/or password for user (%s)',
                                request.form.get('username'))
    return render_template('login.html', error=error)

def valid_login(username, password):
    # mysql
    MYSQL_DATABASE_HOST = os.getenv('IP', '0.0.0.0')
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'my_flask_app'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        passwd=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
        )
    cursor = conn.cursor()
    cursor.execute("SELECT * from minion WHERE username='%s' AND password='%s'" %
                    (username,password))
    data = cursor.fetchone()

    if data:
        return True
    else:
        return False

    # if username == password:
    #     return True
    # else:
    #     return False

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    #  username = request.cookies.get('username')
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('port', 5000))
    app.debug = True
    app.secret_key = '\xa7\x1f\xe3K\xfc\xa1\xb1\xa7&|f\xca\xdf\xe8\x9e9u\xb5\xc7\xcd"+\xd7='# encodes sessions

    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.run(host=host, port=port)
