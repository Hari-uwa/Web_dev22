
from importlib import import_module
from flask import render_template
from app import app
from app import dummy

@app.route('/')
@app.route('/index')
def index():
    
    target= dummy.math()[1]
    return render_template("skeleton.html",target=target)
