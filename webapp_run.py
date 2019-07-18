"""
Leon Santen

This code runs the web application and accesses MixBase.py / run.py. MixBase.py is for development purposes. run.py is for usage purposesself.

Please set the debug_mode to 0 for "off" and 1 for "on".
To STOP server: hit ctrl+c terminal.
"""

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '6fd5dd298e9002621b7e3c76bbf86372' #to get a random key: >>> python, >>> import secrets, >>> secrets.token_hex(16)


@app.route('/') #'/' tells us that it's the index of a page | access via  http://127.0.0.1:5000/
def home():
    return render_template('index.html', title="Home")

#DEBUG Routes
"""@app.route('/hello') # access via  http://127.0.0.1:5000/hello/anything
def hello():
    return render_template('hello.html')"""

@app.route('/hello/<name>') # access via  http://127.0.0.1:5000/hello/*anything*
def helloTemplate(name=None):
    return render_template('hello.html', name=name, title="Debug Route")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    webbrowser.open_new("http://127.0.0.1:5000/")
