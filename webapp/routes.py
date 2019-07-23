from flask import render_template, url_for, flash, redirect
from datetime import datetime
from webapp import app, db, bcrypt
from webapp.forms import RegistrationForm, LoginForm
from webapp.models import User, Pair


@app.route('/') #'/' tells us that it's the index of a page | access via  http://127.0.0.1:5000/
def home():
    return render_template('index.html', title="Home")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # hashes entered password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # create user instance with input from form
        db.session.add(user)
        db.session.commit() # adds user to database
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@mixbase.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger') #danger makes return red #TODO: get success and danger colored frames working
    return render_template('login.html', title='Login', form=form)

#DEBUG Routes
@app.route('/hello') # access via  http://127.0.0.1:5000/hello/anything
def hellos():
    return render_template('hello.html')

@app.route('/hello/<name>') # access via  http://127.0.0.1:5000/hello/*anything*
def helloTemplate(name=None):
    return render_template('hello.html', name=name, title="Debug Route")
