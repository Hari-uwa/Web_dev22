from flask import render_template, redirect, url_for
from app import app, db
from flask_login import current_user, login_required
from app.controllers import GameController, UserController, QuizController


@app.route('/')
@app.route('/index')
@login_required
def index():
    if not current_user.is_authenticated:
        return render_template("login.html")
    return render_template("skeleton.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return UserController.login()
    

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return UserController.register()

@app.route('/logout', methods=['GET','POST'])
def logout():
    return UserController.logout()

@app.route('/statistic', methods=['POST'])
@login_required
def updateStat():
    return GameController.updateStat()


@app.route('/statistic', methods=['GET'])
@login_required
def sendStat():
    return GameController.sendStat()
    #Send stat using sql
    

@app.route('/equation')
@login_required
def equation():
    return QuizController.equation()

