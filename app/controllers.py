from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, RegistrationForm
from app.models import User,Quiz,Game
from datetime import date

class UserController():

    def login():
        form = LoginForm()
        if form.validate_on_submit(): #will return false for a get request
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
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

class GameController():

    def updateStat():
        userId = current_user.id
        data = request.get_json()
        print(data)
        quizId = data['quizId']
        duration = data['duration']
        success = data['success']
        game = Game(user_id=userId, quiz_id=quizId, success=success, duration=duration)
        db.session.add(game)
        db.session.flush()
        db.session.commit()
        return 'updated!'

    def sendStat():
        # Data format: {players:<totalPlayer>,winners:<totalWinner>,shortestTime:<shortestTime>}
        quiz_id = request.args.get("quiz_id")
        totalPlayer = Game.query.filter(Game.quiz_id==quiz_id).count()
        totalWinner = Game.query.filter(Game.quiz_id==quiz_id).filter(Game.success == True).count()
        if (totalWinner != 0):
            shortestTime = Game.query.filter(Game.quiz_id==quiz_id).filter(Game.success == True).order_by(Game.duration).first().duration
            return {"players":totalPlayer,"winners":totalWinner, "shortestTime":shortestTime}
        else:
            return {"players":totalPlayer,"winners":totalWinner, "shortestTime":0}

class QuizController():

    def equation():
        ref = date(2022,5,26)
        today = date.today()
        index = (today-ref).days

        return_object = {}
        current_quiz = Quiz.query.filter(Quiz.quiz_id == index).first()
        return_object["equation"] = current_quiz.pretty_equation()
        return_object["quiz_id"] = index

        return return_object