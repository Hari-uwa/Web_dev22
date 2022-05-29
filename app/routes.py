from datetime import date
from flask import render_template
from app.models import User,Quiz,Game #imports all tables

from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.controllers import UserController
from flask import request

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
def updateStat():
    # return UserController.updateStat()
    #Update database using sql
    # userId = current_user.id
    data = request.get_json() or {}
    print(data)
    # quizId = data['quizId']
    # duration = data['duration']
    # success = data['success']
    # # userId = User.query.filter(Quiz.username==username).first().id
    # game = Game(user_id=1, quiz_id=quizId, success=success, duration=duration)
    # db.session.add(game)
    # db.session.flush()
    # db.session.commit()
    return 'updated!'

@app.route('/statistic', methods=['GET'])
def sendStat():
    return UserController.sendStat()
    #Send stat using sql
    

@app.route('/equation')
def equation():
    ref = date(2022,5,26)

    today = date.today()

    index = (today-ref).days

    return_object = {}
    current_quiz = Quiz.query.filter(Quiz.quiz_id == index).first()
    return_object["equation"] = current_quiz.pretty_equation()
    return_object["quiz_id"] = index
    

    return return_object
