"""
    https://sun.iwu.edu/~mliffito/flask_tutorial/index.html
    Flaskr
    ~~~~~~

    This file uses code adapted from the flaskr flask tutorial which is a micro blog application written as Flask tutorial with flask and sqlite3

    Register, login and logout functions are adapted from a tutorial article from geeks for geeks written bt venniladeenan
    URL : https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
"""

# all the imports
import os, random, werkzeug, csv
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, send_from_directory, flash, session

app = Flask(__name__) # create the application instance :)

# Load default config and override config from an environment variable
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
    # select a random row from the challengeText table
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
    # check if username and paswoord were submitted in the post request
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        db = get_db()

        # find a user in the database with the submmited username
        cur = db.execute('select * from users where username = ?', [username])
        account = cur.fetchone()

        # if a user is found, than that username already exits and prompt the user to choose a different username.
        if account:
            flash('Username already exists! Please chooses a different username')
            return redirect(url_for('registerpage'))
        elif not username or not password:
            flash('Please fill out the required fields!')
            return redirect(url_for('registerpage'))
        # if it's a new username, then enter that username and hashed password into the users table
        else:
            db.execute('INSERT INTO users (username, password) values (?, ?)',
                       [request.form['username'],
                        (werkzeug.security.generate_password_hash(password,
                                                                  method='pbkdf2:sha256',
                                                                  salt_length=16))])
            db.commit()
            flash('You have successfully signed up. Please Sign in to continue')
            return redirect(url_for('registerpage'))

    # if an empty form is submitted then prompt the user to fill the required fields.
    elif request.method == 'POST':
        flash('Please fill out the required fields!')
        return redirect(url_for('registerpage'))
    else:
        flash('Please fill out the required fields!')
        return redirect(url_for('registerpage'))


# This function logs a user given a username and password.
@app.route('/login', methods=['POST'])
def login():
    db = get_db()

    # check if username and password were submitted
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur = db.execute('Select * FROM users where username = ?', [username])
        account = cur.fetchone()

        # check the submitted username and password agains the users in the users table.
        if account:
            pass_check = werkzeug.security.check_password_hash(account['password'], password)
            # if username and password are correct then set the appropriate session keys to their corresponding values in the database
            # for the logged in user and redirect to the home page
            if pass_check:
                session['logged_in'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                session['isadmin'] = account['isadmin']
                flash('Signed in successfully !')
                return redirect(url_for('show_index'))
            # otherwise flash the appropriate error message and redirect to the login page
            else:
                flash('Incorrect username / password !')
                return redirect(url_for('loginpage'))
        elif not username or not password:
            flash('Please fill out the required fields!')
            return redirect(url_for('loginpage'))
        else:
            flash('Incorrect username / password !')
            return redirect(url_for('loginpage'))
    else:
        flash('Please fill out the required fields!')
        return redirect(url_for('loginpage'))


@app.route('/logout')
def logout():
    # delete all the session keys form the session dict
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('isadmin', None)
    flash("Signed out successfully")
    return redirect(url_for('show_index'))


@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/registerpage')
def registerpage():
    return render_template('register.html')


@app.route('/leaderboard')
def leaderBoard():
    db = get_db()
    # get all users order by highscore in descending order
    cur = db.execute('select * from users order by highscore desc')
    leaders = cur.fetchall()
    cur = db.execute('select * from users order by id asc')
    order = cur.fetchall()
    return render_template('leaderboard.html', leaders_order=zip(leaders, order))


@app.route('/profile')
def profile():
    # get username of logged in user from quesry string
    username = request.args.get('user_profile')
    db = get_db()

    # get all the attempts for that user
    cur = db.execute('select * from attempts where user = ? order by id DESC', [username])
    attempts = cur.fetchall()
    count = 0
    sum_wpm = 0
    sum_acc = 0

    # if that user has attempted challlenges, then get thier highscore and calculate their avrage wpm and accuracy
    if attempts:
        cur = db.execute('select * from users where username = ?', [username])
        account = cur.fetchone()
        highscore = account['highscore']
        for i in attempts:
            sum_wpm = sum_wpm + i['acc_wpm']
            sum_acc = sum_acc + i['accuracy']
            count = count + 1
        avg_wpm = round(sum_wpm / count, 2)
        avg_acc = round(sum_acc / count, 2)
        return render_template('profile.html', attempts=attempts, avg_wpm=avg_wpm, avg_acc=avg_acc, highscore=highscore)
    else:
        return render_template('profile.html', attempts=attempts, avg=0, avg_acc=0, highscore=0)


@app.route('/check_highscore', methods=['POST'])
def check_highscore():
    # get the score from the latest attempt and username
    score = int(request.form['highscore'])
    user_id = request.form['user_id']
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE id = ?', [user_id])
    account = cur.fetchone()

    # check if score is greater than the current highscore in the database. if it is then update the highscore in the databse
    if (score > account['highscore']):
        db.execute('UPDATE users SET highscore = ? WHERE id = ?', [score, user_id])
        db.commit()
        return ""
    else:
        return ""


@app.route('/attempts', methods=['POST'])
def addAttempts():
    # get all the results from the challenge and its date
    wpm = request.form['wpm']
    accuracy = request.form['acc']
    acc_wpm = request.form['acc_wpm']
    user = request.form['user_name']
    date = request.form['date']
    db = get_db()

    # insert them into the database
    db.execute('INSERT INTO attempts (user,wpm,accuracy,acc_wpm,date) VALUES(?,?,?,?,?)',
               [user, wpm, accuracy, acc_wpm, date])
    db.commit()
    return ""


@app.route('/add_challenge_text')
def add_text():
    return render_template('addtext.html')


@app.route('/submit_challenge_text', methods=['POST'])
def submit_text():
    db = get_db()

    # insert the text from the form into the database
    db.execute('INSERT INTO challengeText (title,text) VALUES("challengetext",?)',
               [request.form['text']])
    db.commit()
    flash('Challenge text added successfully')
    return redirect(url_for('add_text'))
