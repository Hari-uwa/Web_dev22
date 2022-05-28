from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User
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
            user = User(username=form.username.data, played = 0, max_streak = 0, current_streak = 0, big_tree = 0, tree = 0, plant = 0, small_plant = 0, seed = 0)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

    def updateStat():
        username = current_user.username
        data = request.get_json()
        # Data format: {duration:<duration>,success:<true/false>,acheivement:<"bigtree"/"tree"/"plant"/"smallplant"/"seed">}
        # Update user table and game table
    
    def sendStat():
        # Data format: {totalPlayer:<totalPlayer>,totalWinner:<totalWinner>,shortestTime:<shortestTime>}