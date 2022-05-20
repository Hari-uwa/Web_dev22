from app import db

class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    IP = db.Column(db.String(64), index=True, unique=True)
    
class Quiz(db.Model):
    QuizID = db.Column(db.Integer, primary_key=True)
    EquationText = db.Column(db.String(64), index=True, unique=True)
    IndexNumber = db.Column(db.String(120), index=True, unique=True)

class Practise(db.Model):
    PractiseID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, primary_key=True)
    QuizID = db.Column(db.Integer, primary_key=True)
    AccessTime = db.Column(db.String(64), index=True, unique=True)
    FinishTime = db.Column(db.String(64), index=True, unique=True)
 

    def __repr__(self):
        return '<User {}>'.format(self.username)