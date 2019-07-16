"""
Leon Santen

This code runs the web application and accesses MixBase.py / run.py. MixBase.py is for development purposes. run.py is for usage purposesself.

Please set the debug_mode to 0 for "off" and 1 for "on".
To STOP server: hit ctrl+c terminal.
"""

from flask import Flask
from flask import render_template # to render HTML
app = Flask(__name__)

@app.route('/') #'/' tells us that it's the index of a page | access via  http://127.0.0.1:5000/
def hello_world():
    return render_template('index.html')



#DEBUG Routes
@app.route('/hello') # access via  http://127.0.0.1:5000/hello/anything
def hello():
    return render_template('hello.html')

@app.route('/hello/<name>') # access via  http://127.0.0.1:5000/hello/*anything*
def helloTemplate(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)