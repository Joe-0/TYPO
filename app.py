"""
    https://sun.iwu.edu/~mliffito/flask_tutorial/index.html
    Flaskr
    ~~~~~~

    This file uses code adapted from the flaskr flask tutorial which is a micro blog application written as Flask tutorial with flask and sqlite3

"""

import os, werkzeug
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, send_from_directory, flash

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'typo.db'),
    DEBUG=True,
    SECRET_KEY='development key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.route('/')
def show_index():
    # random_id = random.randint(1, 4)
    db = get_db()
    ##IMPORTANT, THE BOTTOM "id = 1" IS ONLY A TEMPORARY MEASURE CHANGE IT TO RANDOM ID
    # WHEN WE ACTUALLY HAVE TEXT"

    cur = db.execute('SELECT * FROM challengeText ORDER BY RANDOM() LIMIT 1')
    texts = cur.fetchone()
    return render_template('index.html', texts=texts)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# This function takes a username and password input and (hopefully) securely stores them into a users database
@app.route('/register', methods=['POST'])
def register():
    db = get_db()
    ##the following code will enter a new username and a hashed version of a new password into users.
    # note that this function does not check for repeats of the same username
    db.execute('insert into users (username, password) values (?, ?)',
               [request.form['register_username'],
                (werkzeug.security.generate_password_hash(request.form['register_password'], method='pbkdf2:sha256',
                                                          salt_length=16))])
    db.commit()
    return redirect(url_for('show_index'))


# This function logs a user given a username and password. Not quite sure which website to redirect to.
@app.route('/login', methods=['POST'])
def login():
    db = get_db()
    password = db.execute('select password from users where username = ?', request.form['login_username'])
    if werkzeug.security.check_password_hash(password, request.form['login_password']) == True:
        flash('login successful')
        return redirect(url_for('show_index'))

    # case where the password(or username) was wrong
    elif werkzeug.security.check_password_hash(password, request.form['login_password']) == False:
        flash('incorrect password')



@app.route('/attempts')
def fetchAttempts():
    db = get_db()
    cur = db.execute('select * from attempts where users == ? order by id', request.form['user'])
    attempts = cur.fetchall()

    # make render template will redirect to an html page that will show the attempts
    # return render_template('show_entries.html', entries=entries, distinct=distinct)


@app.route('/leaderboard')
def leaderBoard():
    return render_template('leaderboard.html')


@app.route('/add_challenge_text')
def add_text():
    return render_template('addtext.html')


@app.route('/submit_challenge_text', methods=['POST'])
def submit_text():
    db = get_db()
    db.execute('INSERT INTO challengeText (title,text) VALUES("challengetext",?)',
               [request.form['text']])
    db.commit()
    flash('Challenge text added successfully')
    return redirect(url_for('add_text'))


@app.route('/logout')
def logout():
    # logout code here

    return render_template('login.html')
