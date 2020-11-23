#!flask/bin/python
''' runs a flask app
'''
# standard imports
import os, sys
import webbrowser
import json
import datetime
# Flask app imports
from flask import Flask
from flask import request, session
from flask import render_template
from flask import flash, redirect, url_for
from flask.json import JSONEncoder
from werkzeug.utils import secure_filename
# origami viewer imports
###

# constants
ALLOWED_EXTENSIONS = {'png', 'jpg'}

# functions ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# setup app
#if getattr(sys, 'frozen', False):
template_folder = resource_path('templates')
static_folder = resource_path('static')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
#else:
#    app = Flask(__name__, static_folder='origami/static')

# configure app
# need secret key for session
app.config['SECRET_KEY'] = 'origami'

# define app routes
@app.route('/', methods=['GET'])
def landing():
    return redirect(url_for('forest'))

@app.route('/natalieholmes', methods=['GET'])
def home():
    if request.method == 'GET':
        # render template
        return render_template('site/holmes.html')

@app.route('/space', methods=['GET'])
def space():
    if request.method == 'GET':
        # render template
        return render_template('site/space.html')

@app.route('/forest', methods=['GET'])
def forest():
    if request.method == 'GET':
        # render template
        return render_template('site/forest.html')

@app.route('/snow', methods=['GET'])
def snow():
    if request.method == 'GET':
        # render template
        return render_template('site/snow.html')

@app.route('/sea', methods=['GET'])
def sea():
    if request.method == 'GET':
        # render template
        return render_template('site/sea.html')

# if run as main then run app
if __name__ == '__main__':
    # print info
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!                                                                             !!!')
    print('!!! origami will perform best if your default browser is Google Chrome   !!!')
    print('!!!                                                                             !!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    # open html at IP address 127.0.0.1 (should be default)
    #webbrowser.get().open('http://127.0.0.1:8010/origami', new=1)
    app.run(host='0.0.0.0', port = 8010)
