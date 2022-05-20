from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    max_streak = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.max_streak)

