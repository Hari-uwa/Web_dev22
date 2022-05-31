import sys
sys.path.append("..") # allows for the previous directory to be searched too

from app import db
from app.models import Quiz,User,Game #imports Quiz table
from sqlalchemy import exc
import random

def bidmas_calc(input):
    equ = "".join(input)
    return eval(equ)

def equation(): #generates a random equation as comma separated string
    while 1:
        output = [] 
        ops = ['+', '-', '*', '/']
    
        for i in range(8): #creates a random list with 8 numbers
            n = random.randint(1,9)
            output.append(str(n))
    
        operation1 = random.choice(ops)
        operation2 = random.choice(ops)
        output[2] = operation1
        output[5] = operation2
        
        try:
            target=bidmas_calc(output)
        except ZeroDivisionError: 
            pass
        if type(target)!=float: # validator to only end while-loop when an equation has an integer answer
            output.append(str(target))                   
            break
            
    out_str=','.join(output) #converts the list to a comma separated string
    return out_str

# use to upload equations to Quiz Table
def main(args):
    quizNum = 1
    lastQuizId = Quiz.query.order_by(Quiz.quiz_id.desc()).first().quiz_id

    if len(args) > 0:
        quizNum = int(args[0])

    for i in range(quizNum): #set range of quiz_id
        try:                   
            eq = equation()
            quizId = lastQuizId + i + 1
            q = Quiz(quiz_id=quizId, equation=eq)
            db.session.add(q)
            db.session.commit()
            print("Quiz:", quizId, "Equation:", eq)
        except exc.IntegrityError:
            print("IntegrityError")
            pass
        except exc.PendingRollbackError:
            print("PendingRollbackError")
            db.session.rollback()

# Take one argument as number of quiz to add, if no argument is given will add 1 quiz
if __name__ == "__main__":
   main(sys.argv[1:])