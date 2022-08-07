# All of the imports
from crypt import methods
import os
import requests

from flask import Flask, flash, g, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from forms import JournalEntryForm, RegistrationForm, UserLoginForm, QuestionnaireForm

from models import Questions, db, connect_db, User, Journal

CURR_USER_KEY = "curr_user"

app = Flask(__name__)
CORS(app)

# Get DB_URI from environ variable
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///mentalkeep_db'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "super secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)





########################## Global Request ################################

@app.before_request
def add_to_global():
    """Adding the user to the Flask global"""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    
    else:
        g.user = None

def do_login(user):
    """Login user"""

    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout user"""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

###########################################################################
# Begin Application

@app.route("/quickjot")
def quick_journal():
    """Quick Journal"""

    return render_template("quickjot.html")


@app.route("/register", methods=["GET", "POST"])
def new_user():
    """New user signup.
    Creates a new user and adds them to the DB.
    Checks to make sure username is unique.
    """
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = RegistrationForm()

    if form.validate_on_submit():
        try:
            user = User.register(
                username = form.username.data,
                password = form.password.data,
                image_url = form.image_url.data or User.image_url.default.arg,
            )
            db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('register.html', form=form)

        do_login(user)

        return redirect("/")
    
    else:
        return render_template('register.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    """User Login"""

    form = UserLoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            do_login(user)
            flash(f"Welcome, {user.username}", 'success')
            return redirect("/")

        flash("Try again. Invalid credentials.", 'danger')

    return render_template('/login.html', form=form)

@app.route('/logout')
def logout():
    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")
# User profile and new journal entries

@app.route("/")
def home_page():
    """Quote of the Day API call"""
    resp = requests.get("https://zenquotes.io/api/today/")

    quote_data = resp.json()
    quote_q = quote_data[0]['q']
    author_a = quote_data[0]['a']
    quote = quote_q
    author = author_a
    

    if g.user:

        return render_template('home.html')
    else:
        return render_template('base.html', quote=quote, author=author)


@app.route("/journal/new", methods=["GET", "POST"])
def add_journal_entry():
    """Add a journal entry"""

    if not g.user:
        flash("Access Denied", "danger")
        return redirect('/')
    
    form = JournalEntryForm()

    if form.validate_on_submit():
        title = form.title.data
        entry = form.entry.data

        journal = Journal(
            title = title,
            entry = entry  
        )

        g.user.journals.append(journal)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("journal/new.html", form=form)

@app.route("/phq9")
def phq9_test():
    """Start PHQ9 test"""

    if not g.user:
        flash("Access Denied. Please register", "danger")
        return redirect("/register")
    else:
        questions = Questions.query.all()

        return render_template("phq9.html", questions=questions)

@app.after_request
def no_cache_headers(req):
    """Add no-caching headers"""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers["Cache-Control"] = "public, max-age=0"
    return req