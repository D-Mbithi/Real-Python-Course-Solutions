import sqlite3
from functools import wraps
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for
    )


# config
app = Flask(__name__)
app.config.from_object('_config')


# helper functions
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)

        flash('You need to login first')
        return redirect(url_for('login'))
    return wrap

# route handler functions
@app.route('/')
@login_required
def home():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Login again.'
            return render_template('login.html', error=error)
        session['logged_in'] = True
        flash('Welcome.')
        return redirect(url_for('home'))
    return render_template('login.html')
