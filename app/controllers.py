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
            user = User(username=form.username.data, played = 0, max_streak = 0, current_streak = 0, big_tree = 0, tree = 0, plant = 0,small_plant = 0, seed = 0)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

    def updateUserStat():
        userId = current_user.id
        data = request.get_json()
        print(data)
        quizId = data['quizId']
        duration = data['duration']
        success = data['success']

        # Get user
        user = User.query.filter_by(id=userId).first()

        # Update number of game played by user
        user.played = user.played + 1

        # Update user's plant colletion
        if (success):
            if duration < 30:
                user.big_tree += 1
            elif duration <60:
                user.tree += 1
            elif duration <90:
                user.plant += 1
            elif duration < 120:
                user.small_plant += 1
            else:
                user.seed += 1
        
        # Update user's streak and max streak
        lastQuizWon = Game.query.filter(Game.user_id==userId).filter(Game.success == True).order_by(Game.quiz_id.desc()).first()
        if lastQuizWon is not None:
            lastQuizId = lastQuizWon.quiz_id
            if quizId == lastQuizId + 1:
                user.streak += 1
            else:
                user.streak = 0
        if user.max_streak < user.streak:
            user.max_streak = user.streak
        
        db.session.commit()
        return 'updated!'

class GameController():

    def updateGameStat():
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