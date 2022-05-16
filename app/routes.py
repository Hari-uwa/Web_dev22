
from importlib import import_module
from flask import render_template
from app import app
from app import python_scripts

@app.route('/')
@app.route('/index')
def index():
    
    target= python_scripts.dummy.py
    return render_template("skeleton.html",target=target)
