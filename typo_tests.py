"""
https://sun.iwu.edu/~mliffito/flask_tutorial/testing.html
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.

    paragraphs for the challenge texts were obtained from Random Paragraph generator https://randomwordgenerator.com/paragraph.php
"""
import os
import app as flaskr
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])


    def register(self, username, password):
        return self.app.post('/register', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_show_index(self):
        rv = self.app.get('/')
        assert b'Begin typing when ready' in rv.data

    def test_leaderboard(self):
        rv = self.app.get('/leaderboard')
        assert b'Rankings' in rv.data
        assert b'Username' in rv.data
        assert b'Highest Accurate WPM' in rv.data

    def test_add_text(self):
        rv = self.app.get('/add_challenge_text')
        assert b'Add New challenge Text' in rv.data
        assert b'Type challenge text here' in rv.data

    def test_profile_page(self):
        rv = self.app.get('/profile')
        assert b'User Profile' in rv.data

    def test_login_page(self):
        rv = self.app.get('/loginpage')
        assert b'Welcome back to Typo !' in rv.data
        assert b"Don't have an account?" in rv.data
        assert b"Username" in rv.data
        assert b"Password" in rv.data

    def test_register_page(self):
        rv = self.app.get('/registerpage')
        assert b'Sign up for Typo !' in rv.data
        assert b"Already have an account?" in rv.data
        assert b"Username" in rv.data
        assert b"Password" in rv.data

    def test_register_login_logout(self):
        rv = self.register('admin', 'default')
        assert b'You have successfully signed up. Please Sign in to continue' in rv.data
        rv = self.register('admin', 'default')
        assert b'Username already exists! Please chooses a different username' in rv.data
        rv = self.register(None, None)
        assert b'Please fill out the required fields!' in rv.data
        rv = self.register('', '')
        assert b'Please fill out the required fields!' in rv.data
        rv = self.login('admin', 'default')
        assert b'Signed in successfully !' in rv.data
        rv = self.logout()
        assert b'Signed out successfully' in rv.data
        rv = self.login('', '')
        assert b'Please fill out the required fields!' in rv.data
        rv = self.login('adminx', 'default')
        assert b'Incorrect username / password !' in rv.data
        rv = self.login('admin', 'defaultx')
        assert b'Incorrect username / password !' in rv.data


