"""
https://sun.iwu.edu/~mliffito/flask_tutorial/testing.html
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import os
import app as flaskr
import unittest
import tempfile


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)

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

    def test_show_index(self):
        rv = self.app.get('/')
        assert b'Begin typing when ready' in rv.data

    def test_register(self):
        rv = self.app.post('/register', data=dict(
            username='Yo',
            password='not'
        ), follow_redirects=True)

        assert b'Yo' in rv.data
        assert b'not' in rv.data

    def test_login_logout(client):
        """Make sure login works."""
        username = flaskr.app.config["USERNAME"]
        password = flaskr.app.config["PASSWORD"]

        rv = login(client, username, password)
        assert b'You were logged in' in rv.data

        rv = login(client, username, f'{password}x')
        assert b'Invalid password' in rv.data

        rv = logout(client)
        assert b'You were logged out' in rv.data
