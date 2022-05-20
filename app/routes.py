
from importlib import import_module
from flask import render_template
from app import app
from app import eqn_gen

@app.route('/')
@app.route('/index')
def index():
    
    target= eqn_gen.math()[1][-1]
    return render_template("skeleton.html",target=target)
