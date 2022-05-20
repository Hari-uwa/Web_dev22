from datetime import datetime
from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    max_streak = db.Column(db.Integer)

    posts = db.relationship('Game', backref='player', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.max_streak)

class Quiz(db.Model):
    quiz_id = db.Column(db.Integer, primary_key=True)
    equation= db.Column(db.VARCHAR(45))

    posts = db.relationship('Game', backref='challenge', lazy='dynamic')

    def __repr__(self):
        return '<Quiz {}>'.format(self.equation)

class Game(db.Model):
    game_id = db.Column(db.VARCHAR(45), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    quiz_id = db.Column(db.Integer,db.ForeignKey('quiz.quiz_id'))
    outcome = db.Column(db.Boolean)
    duration = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Quiz {}>'.format(self.duration)

