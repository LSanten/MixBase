"""
Leon Santen

This code runs the web application and accesses MixBase.py / run.py. MixBase.py is for development purposes. run.py is for usage purposesself.

Please set the debug_mode to 0 for "off" and 1 for "on".
To STOP server: hit ctrl+c terminal.
"""

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '6fd5dd298e9002621b7e3c76bbf86372' #to get a random key: >>> python, >>> import secrets, >>> secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webmix.db' # create database named "webmix.db"
db = SQLAlchemy(app) # create database instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pair_posts = db.relationship('Pair', backref='author', lazy=True) #this is a releationship not a column -- backreference to Pair. You can find out author of a pair post by using pair.author #lazy=True --> sqlalchemy will load data directly when used

    def __repr__(self):
        return f"User('{self.username}')"

class Pair(db.Model): #data table for transition pair
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    secondname = db.Column(db.String(30), nullable=False)
    firstartist = db.Column(db.String(30), nullable=False)
    secondtartist = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Pair('{self.firstname}', '{self.secondname}', '{self.date_posted}' )"



@app.route('/') #'/' tells us that it's the index of a page | access via  http://127.0.0.1:5000/
def home():
    return render_template('index.html', title="Home")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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



if __name__ == '__main__':
    app.run(debug=True)
    webbrowser.open_new("http://127.0.0.1:5000/")
