# controller for blog

#imports
from flask import (
        Flask,
        render_template,
        request,
        session,
        url_for,
        flash,
        redirect,
        g
        )
import sqlite3
from functools import wraps


# Comfiguration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'qwertyuiop1234567890'


app = Flask(__name__)

app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        flash('You need to login first')
        return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200

    if request.method == "POST":
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))

    return render_template('login.html', error=error), status_code


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    flash('You have logout')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
