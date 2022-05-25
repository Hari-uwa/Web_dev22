import sys

sys.path.append("..") # allows for the previous directory to be searched too

from app import db
from app.models import User,Quiz,Game #imports all tables
from sqlalchemy import func
from datetime import date

ref= date(2022,5,4)

today=date.today()

index= (today-ref).days

userquiz = Quiz.query.filter(Quiz.quiz_id==index).first()

numbers = userquiz.equation.split(',')

lst = [0,1,3,4,6,7,8]
for i in lst:
    numbers[i]= int(numbers[i])
    
dict = {}
for i in range(9):
    dict[i]=numbers[i]

import json                                
json_object = json.dumps(dict, indent = 4) # Serializing json 
print(json_object) ## jsonify to python dictionary