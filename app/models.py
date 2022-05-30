from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique = True)
    password_hash = db.Column(db.String(128))
    played = db.Column(db.Integer)
    win = db.Column(db.Integer)
    max_streak = db.Column(db.Integer)
    current_streak = db.Column(db.Integer)
    big_tree = db.Column(db.Integer)
    tree = db.Column(db.Integer)
    plant = db.Column(db.Integer)
    small_plant = db.Column(db.Integer)
    seed = db.Column(db.Integer)
    games = db.relationship('Game', backref='player', lazy='dynamic')

    def __repr__(self):
        return '<User {}, username:{}, played:{}, win:{} max_streak:{}, current_streak:{}>'.format(self.id, self.username, \
        self.played, self.win, self.max_streak, self.current_streak)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Quiz(db.Model):
    quiz_id = db.Column(db.Integer, primary_key=True)
    equation= db.Column(db.VARCHAR(45))

    games = db.relationship('Game', backref='challenge', lazy='dynamic')

    def __repr__(self):
        return '<Quiz {}, equation:{}>'.format(self.quiz_id, self.equation)

    def pretty_equation(self):
        split = self.equation.split(',')
        return_list = [ int(i) if self.checkInt(i) else i for i in split]
        return return_list

    def checkInt(self, test_string : str):
        try : 
            int(test_string)
            return True
        except ValueError:
            return False
    

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quiz_id = db.Column(db.Integer,db.ForeignKey('quiz.quiz_id'))
    success = db.Column(db.Boolean)
    duration = db.Column(db.Integer)

    def __repr__(self):
        return '<Game game_id:{}, user_id:{}, quiz_id:{}, success:{}, duration:{}'.format(self.game_id, \
        self.user_id,self.quiz_id,self.success, self.duration)
