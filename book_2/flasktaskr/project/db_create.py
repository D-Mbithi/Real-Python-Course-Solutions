from datetime import date
from views import db
from models import Task

# create database and the table
db.create_all()

# database population
# db.session.add(Task('Finish this tutorial.', date(2019, 9, 22), 10, 1))
# db.session.add(Task('Start flask project.', date(2019, 1, 2), 8, 1))
# db.session.add(Task('Deploy django project.', date(2019, 10, 14), 9, 1))
# db.session.add(Task('Scrape ett.tv website', date(2019, 4, 4), 2, 1))

# commit session
db.session.commit()
