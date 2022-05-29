from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User,Quiz,Game
from flask import request
from datetime import datetime

class UserController():

    def login():
        form = LoginForm()
        if form.validate_on_submit(): #will return false for a get request
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('invalid username or password')
                return redirect(url_for('login'))
            login_user(user,remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html',title='Sign In', form = form)

    def logout():
        logout_user()
        return redirect(url_for('login'))

    def register():
        form= RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

    #TODO: complete this function, data received will be of the following format. Need to update game table using the data
    # Query Logic:
    # Update user SET played += 1, tree += 1, streak 
    # data: { quizId: quizId, duration: timeTaken, success: solved }
    def updateStat():
        userId = current_user.id
        data = request.get_json()
        print(data)
        quizId = data['quizId']
        duration = data['duration']
        success = data['success']
        # userId = User.query.filter(Quiz.username==username).first().id
        game = Game(user_id=1, quiz_id=quizId, success=success, duration=duration)
        db.session.add(game)
        db.session.flush()
        db.session.commit()
        return 'updated!'


    #TODO: complete this function, data to return will be of following format. Need to query game table to get the data.
    # Query Logic:
    # totalPlayer = SELECT COUNT(*) WHERE quiz_id = <id> and success = true
    # totalWinner = SELECT COUNT(*) WHERE quiz_id - <id>
    # shortestTime = SELECT duration WHERE quiz_id = <id> and success = true SORT BY duration LIMIT 1
    # front end may be able to attach quiz_id as parameter of the GET request
    def sendStat():
        # Data format: {players:<totalPlayer>,winners:<totalWinner>,shortestTime:<shortestTime>}
        # return the aboove data format
        quiz_id = request.args.get("quiz_id")
        totalPlayer = Game.query.filter(Game.quiz_id==quiz_id).count()
        totalWinner = Game.query.filter(Game.quiz_id==quiz_id).filter(Game.success == True).count()
        shortestTime = Game.query.filter(Game.quiz_id==quiz_id).filter(Game.success == True).order_by(Game.duration).first().duration
        if totalPlayer is not None:
            return {"players":totalPlayer,"winners":totalWinner, "shortestTime":shortestTime}
        else:
            return {"players":0,"winners":0, "shortestTime":0}