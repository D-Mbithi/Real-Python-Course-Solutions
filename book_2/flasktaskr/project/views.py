import sqlite3
from functools import wraps
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for, g
    )
from forms import AddTaskForm

# config
app = Flask(__name__)
app.config.from_object('_config')


# DB connection function
def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


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

# logout function
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye')
    return redirect(url_for('home'))


# login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Login again.'
            return render_template('login.html', error=error)
        session['logged_in'] = True
        flash('Welcome.')
        return redirect(url_for('home'))
    return render_template('login.html')


# view tasks
@app.route('/tasks/')
@login_required
def tasks():
    g.db = connect_db()

    cursor = g.db.execute(
        "SELECT name, due_date, priority, task_id FROM tasks WHERE status=1"
    )

    open_tasks = [
        dict(
            name=row[0], due_date=row[1], priority=row[2], task_id=row[3]
        ) for row in cursor.fetchall()
    ]
    cursor = g.db.execute(
        "SELECT name, due_date, priority, task_id FROM tasks WHERE status=0"
    )

    close_tasks = [
        dict(
            name=row[0], due_date=row[1], priority=row[2], task_id=row[3]
        ) for row in cursor.fetchall()
    ]

    g.db.close()
    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks,
        close_tasks=close_tasks
    )


# add tasks
@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    g.db = connect_db()
    name = request.form['name']
    date = request.form['due_date']
    priority = request.form['priority']

    if not name or not date or not priority:
        flash('All fields are required. Please try again.')

        return redirect(url_for('tasks'))

    n_task = [
        request.form['name'],
        request.form['due_date'],
        request.form['priority'],
        ]
    g.db.execute(
        "INSERT INTO tasks(name, due_date, priority, status) VALUES(?,?,?,1)", n_task)
    g.db.commit()
    g.db.close()
    flash("New entry was successfully posted. Thanks.")

    return redirect(url_for('tasks'))


# mark as complete
@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    g.db = connect_db()
    g.db.execute("UPDATE tasks SET status=0 WHERE task_id="+str(task_id))
    g.db.commit()
    g.db.close()
    flash("Task was marked complete.")

    return redirect(url_for('tasks'))



# delete task
@app.route('/delete/<int:task_id>/')
@login_required
def delete_task(task_id):
    g.db = connect_db()
    g.db.execute("DELETE FROM tasks WHERE task_id="+str(task_id))
    g.db.commit()
    g.db.close()
    flash("Task was delete.")

    return redirect(url_for('tasks'))
