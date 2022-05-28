from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for
from datetime import datetime, timedelta
import os

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32), unique = True)
  password_hash = db.Column(db.String(128))
  played = db.Column(db.Integer)
  max_streak = db.Column(db.Integer)
  current_streak =db.Column(db.Integer)
  big_tree =db.Column(db.Integer)
  tree = db.Column(db.Integer)
  plant = db.Column(db.Integer)
  small_plant = db.Column(db.Integer)
  seed= db.Column(db.Integer)
  #token authetication for api
#   token = db.Column(db.String(32), index=True, unique = True)
#   token_expiration=db.Column(db.DateTime)
  games = db.relationship('Game', backref='player', lazy='dynamic')

  def __repr__(self):
    return '<User {}, username:{}>'.format(self.id, self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  ###Token support methods for api

#   def get_token(self, expires_in=30):
#     now = datetime.utcnow()
#     if self.token and self.token_expiration > now + timedelta(seconds=60):
#       return self.token
#     self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
#     self.token_expiration = now+timedelta(days=expires_in)
#     db.session.add(self)
#     return self.token

#   def revoke_token(self):
#     self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

#   @staticmethod
#   def check_token(token):
#     user = User.query.filter_by(token=token).first()
#     if user is None or user.token_expiration < datetime.utcnow():
#       return None
#     return user

  '''Adding in dictionary methods to convert to JSON
     Format
     {
     'id':'19617810',
     'first_name':'Timothy',
     'surname': 'French',
     'prefered_name':'Tim',
     'cits3403':False,
     'pin':'0000',
     '_links':{
       'project': 'api/student/19617810/project'
      }
    }'''

#   def to_dict(self):
#     data = {
#         'username': self.username,
#     }
#     return data

#   def from_dict(self, data):
#     if 'pin' in data :
#       self.set_password(data['pin'])

    
#   def __str__(self):
#     return self.first_name+' '+self.surname





# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     max_streak = db.Column(db.Integer)

#     posts = db.relationship('Game', backref='player', lazy='dynamic')
    
#     def __repr__(self):
#         return '<User {}>'.format(self.max_streak)

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
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Game game_id:{}, user_id:{}, quiz_id:{}, success:{}, duration:{}, date:{}>'.format(self.game_id, \
        self.user_id,self.quiz_id,self.success, self.duration,self.date)
