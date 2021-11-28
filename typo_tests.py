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


    def test_leaderboard(self):
        rv = self.app.get('/leaderboard')
        assert b'Rankings' in rv.data
        assert b'Username' in rv.data
        assert b'Highest Accurate WPM' in rv.data

    def test_add_text(self):
        rv = self.app.get('/add_challenge_text')
        assert b'Add New challenge Text' in rv.data
        assert b'Type challenge text here' in rv.data





