"""
    https://sun.iwu.edu/~mliffito/flask_tutorial/index.html
    Flaskr
    ~~~~~~

    This file uses code adapted from the flaskr flask tutorial which is a micro blog application written as Flask tutorial with flask and sqlite3

    Register, login and logout functions are adapted from a tutorial article from geeks for geeks written bt venniladeenan
    URL : https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
"""

import os, random, werkzeug, csv
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, send_from_directory, flash, session

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
    db.execute('INSERT INTO users (username, password, isadmin) values (?, ?, ?)',
               ['admin1', (werkzeug.security.generate_password_hash('default',
                                                                    method='pbkdf2:sha256',
                                                                    salt_length=16)), True])
    db.commit()


def seed():
    with app.open_resource('challenge_one.csv', mode='r') as chal:
        dr = csv.DictReader(chal)
        challenge_one = [(i['id'], i['title'], i['text']) for i in dr]

    db = get_db()

    db.executemany("insert into challengeText (id, title, text) VALUES (?, ?, ?);", challenge_one)

    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    seed()
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
    db = get_db()
    cur = db.execute('SELECT * FROM challengeText ORDER BY RANDOM() LIMIT 1')
    texts = cur.fetchone()
    return render_template('index.html', texts=texts)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# This function takes a username and password input and (hopefully) securely stores them into a users database
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cur = db.execute('select * from users where username = ?', [username])
        account = cur.fetchone()
        if account:
            msg = 'Username already exists! Please chooses a different username'
        elif not username or not password:
            msg = 'Please fill out the required fields!'
        else:
            db.execute('INSERT INTO users (username, password) values (?, ?)',
                       [request.form['username'],
                        (werkzeug.security.generate_password_hash(password,
                                                                  method='pbkdf2:sha256',
                                                                  salt_length=16))])
            db.commit()
            msg = 'You have successfully signed up. Please Sign in to continue'
    elif request.method == 'POST':
        msg = 'Please fill out the required fields!'
    return render_template('register.html', msg=msg)


# This function logs a user given a username and password. Not quite sure which website to redirect to.
@app.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    cur = db.execute('SELECT * FROM challengeText ORDER BY RANDOM() LIMIT 1')
    texts = cur.fetchone()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur = db.execute('Select * FROM users where username = ?', [username])
        account = cur.fetchone()
        if account:
            pass_check = werkzeug.security.check_password_hash(account['password'], password)
            if pass_check:
                session['logged_in'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                session['highscore'] = account['highscore']
                session['isadmin'] = account['isadmin']
                msg = 'Signed in successfully !'
                return render_template('index.html', msg=msg, texts=texts)
            else:
                msg = 'Incorrect username / password !'
        elif not username or not password:
            msg = 'Please fill out the required fields!'
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    db = get_db()
    cur = db.execute('SELECT * FROM challengeText ORDER BY RANDOM() LIMIT 1')
    texts = cur.fetchone()
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('highscore', None)
    session.pop('isadmin', None)
    msg = "Signed out successfully"
    return render_template('index.html', msg=msg, texts=texts)


@app.route('/attempts')
def fetchAttempts():
    return None


@app.route('/loginpage')
def loginpage():
    return render_template('login.html')


@app.route('/registerpage')
def registerpage():
    return render_template('register.html')


@app.route('/leaderboard')
def leaderBoard():
    db = get_db()
    cur = db.execute('select * from users order by highscore desc')
    leaders = cur.fetchall()
    cur = db.execute('select * from users order by id asc')
    order = cur.fetchall()
    return render_template('leaderboard.html', leaders_order=zip(leaders,order))


@app.route('/profile')
def profile():
    username = request.args.get('user_profile')
    db = get_db()
    cur = db.execute('select * from attempts where user = ? order by id DESC', [username])
    attempts = cur.fetchall()
    return render_template('profile.html', attempts=attempts)


@app.route('/check_highscore', methods=['POST'])
def check_highscore():
    '''score = request.form['highscore']
    if (request.form['highscore']>score):
        db = get_db()
        db.execute('UPDATE users SET highscore = ? WHERE username = ?', [score, session['username']])
        db.commit()
        return ""
    else:
        return ""'''
    score = int(request.form['highscore'])
    user_id = request.form['user_id']
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE id = ?', [user_id])
    account = cur.fetchone()

    if (score > account['highscore']):
        db.execute('UPDATE users SET highscore = ? WHERE id = ?', [score, user_id])
        db.commit()
        session['highscore'] = score
        return ""
    else:
        return ""


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


