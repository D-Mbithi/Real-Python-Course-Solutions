# controller for blog

#imports
from flask import (
        Flask,
        render_template,
        request,
        session,
        flash,
        redirect,
        g
        )
import sqlite3


# Comfiguration
DATABASE = 'blog.db'

app = Flask(__name__)

app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
