# controller for blog

#imports
from functools import wraps
import sqlite3
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
    g.db = connect_db()
    cur = g.db.execute('select * from blog')
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)


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


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        title = request.form['title']
        post = request.form['post']

        if not title or not post:
            flash('All fields need to be field')
            return redirect(url_for('home'))

        g.db = connect_db()
        g.db.execute('INSERT INTO blog VALUES(?,?)', [request.form['title'], request.form['post']])
        g.db.commit()
        g.db.close()
        flash('New post has been successfully posted.')

        return redirect(url_for('home'))

    return render_template('add_post.html')


if __name__ == '__main__':
    app.run(debug=True)
