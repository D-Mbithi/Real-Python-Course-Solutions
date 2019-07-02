import datetime
from functools import wraps
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for
    )
from flask_sqlalchemy import SQLAlchemy
from forms import AddTaskForm, RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError


# config
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object('_config')
db = SQLAlchemy(app)

from models import Task, User


def open_tasks():
    return db.session.query(Task).filter_by(status=1).order_by(Task.due_date.asc())

def closed_tasks():
    return db.session.query(Task).filter_by(status=0).order_by(Task.due_date.asc())

# helper functions
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)

        flash('You need to login first')
        return redirect(url_for('login'))
    return wrap


# ROUTE HANDLER FUNC
#-------------------

# logout function
@app.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Goodbye')
    return redirect(url_for('login'))


# login function
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('Welcome!')
                return redirect(url_for('tasks'))
            else:
                error = 'Invalid username or password.'

        else:
            error = 'Both fields are required.'
    return render_template('login.html', form=form, error=error)


# view tasks
@app.route('/tasks/')
@login_required
def tasks():

    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks(),
        closed_tasks=closed_tasks()
    )


# add tasks
@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    error = None
    form = AddTaskForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Task(
                form.name.data,
                form.due_date.data,
                form.priority.data,
                '1',
                datetime.datetime.utcnow(),
                session['user_id']
            )
            db.session.add(new_task)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('tasks'))
    return render_template('tasks.html', form=form, error=error)


# mark as complete
@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    new_id = task_id
    db.session.query(Task).filter_by(task_id=new_id).update({'status': '0'})
    db.session.commit()
    flash("Task was marked complete.")

    return redirect(url_for('tasks'))


# delete task
@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
    new_id = task_id
    db.session.query(Task).filter_by(task_id=new_id).delete()
    db.session.commit()
    flash("Task was delete.")

    return redirect(url_for('tasks'))


# registeration function
@app.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('login'))
            except IntegrityError:
                flash('The username or email already exist.')
                return render_template('register.html', form=form, error=error)
        print(False)
        print(form.errors)
    return render_template('register.html', form=form, error=error)


def flash_errors(form):
    for field, errors in form.error.items():
        for error in errors:
            flash(u"Error in the %s field - %s " % (getattr(form, field).label.text, error), 'error')
