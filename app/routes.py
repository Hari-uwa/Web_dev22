
from datetime import date
from flask import render_template
from app import app
from app.models import User,Quiz,Game #imports all tables

@app.route('/')
@app.route('/index')
def index():
    
    return render_template("skeleton.html")

@app.route('/equation')
def equation():
    ref = date(2022,5,26)

    today = date.today()

    index = (today-ref).days

    return_object = {}
    current_quiz = Quiz.query.filter(Quiz.quiz_id == index).first()
    return_object["equation"] = current_quiz.pretty_equation()

    return return_object
