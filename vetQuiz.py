import sys

sys.path.append("..") # allows for the previous directory to be searched too

from app import db
from app.models import Quiz #imports Quiz table
from sqlalchemy import exc

quizes = Quiz.query.all()
for quiz in quizes:
    print(quiz)