import os
import unittest

from views import app, db
from _config import BASEDIR
from models import User


TEST_DB = 'test.db'


class AllTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_setup(self):
        new_user = User('michael', 'michael@friction.org', 'michaelman')
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()

        for t in test:
            t.name
        assert t.name == 'michael'

    def test_form_is_present(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please login to access your task list.', response.data)

    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)

    def test_users_cannot_login_if_not_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn(b'Invalid username or password.', response.data)

    def register(self, name, email, password, confirm):
        return self.app.post(
            '/register',
            data=dict(name=name, email=email, password=password, confirm=confirm),
            follow_redirects=True
            )

    def test_user_can_login(self):
        self.register('dennis', 'denmbithi@friction.com', 'friction', 'friction')
        response = self.login('dennis', 'friction')
        self.assertIn(b'Welcome!', response.data)

    def test_invalid_form_data(self):
        self.register('dennis', 'denmbithi@friction.com', 'friction', 'friction')
        response = self.login('newuser', 'newuser')
        self.assertIn(b'Invalid username or password', response.data)

    def test_form_is_present_on_the_register_page(self):
        response = self.app.get('register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please register to access the task list.', response.data)

    def test_user_registered(self):
        self.app.get('register/', follow_redirects=True)
        response = self.register('Michael', 'michael@realpython.com', 'friction', 'friction')
        self.assertIn(b'Thanks for registering. Please login.', response.data)

    def test_user_registration_error(self):
        self.app.get('register/', follow_redirects=True)
        self.register('daniel', 'daniel@realpython.com', 'friction', 'friction')
        self.app.get('register/', follow_redirects=True)
        self.register('daniel', 'daniel@realpython.com', 'friction', 'friction')


    def logout(self):
        return self.app.get('logout/', follow_redirects=True)

    def test_logged_in_user_can_logout(self):
        self.register('fletcher', 'fletcher@gmail.com', 'friction', 'friction')
        self.app.get('login/', follow_redirects=True)
        self.login('fletcher', 'friction')
        response = self.logout()
        self.assertIn(b'Goodbye', response.data)
    
    def test_users_not_logged_in_can_not_logout(self):
        response = self.logout()
        self.assertNotIn(b'Goodbye', response.data)

    def create_user(self, name, email, password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('add/', data=dict(
            name='Go to the bank',
            due_date='24/10/2019',
            priority='6',
            posted_date='10/02/2019',
            status='1'
                ), follow_redirects=True)

    def test_user_can_add_task(self):
        self.create_user('dennis', 'dennis@gmail.com', 'friction')
        self.login('dennis', 'friction')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(
            b'New entry was successfully posted. Thanks.', response.data
                )

    def test_cannot_add_task_when_error(self):
        self.create_user('dennis', 'dennis@gmail.com', 'friction')
        self.login('dennis','friction')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.post('add/', data=dict(
            name='Go to the market',
            due_date='',
            priority='6',
            posted_date='02/06/2019',
            status='7'
            ), follow_redirects=True)
        self.assertIn(b'This field is required', response.data)

    def test_user_can_complete_task(self):
        self.create_user('dennis', 'dennis@gmail.com', 'friction')
        self.login('dennis', 'friction')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('complete/1', follow_redirects=True)
        self.assertIn(
            b'Task was marked complete.', response.data)

    def test_user_can_delete_task(self):
        self.create_user('dennis', 'dennis@gmail.com', 'friction')
        self.login('dennis', 'friction')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('delete/1', follow_redirects=True)
        self.assertIn(
            b'Task was delete.', response.data)

    def test_user_cannot_complete_task_that_are_not_created_by_them(self):
        self.create_user('dennis', 'dennis@gmail.com', 'friction')
        self.login('dennis', 'friction')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_user('daniel', 'daniel@gmail.com', 'friction')
        self.login('daniel', 'friction')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get('complete/1', follow_redirects=True)
        self.assertNotIn(b'Task was marked complete.', response.data)


if __name__ == "__main__":
    unittest.main()
