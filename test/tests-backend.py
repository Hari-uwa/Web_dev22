import sys
sys.path.append('/home/hariv22/coding/webdev_22/project/Web_dev22/') # allows for the previous directory to be searched too


from app import app,db
from app.models import Quiz,User,Game #imports Quiz table
from sqlalchemy import exc
import unittest


class UserModelCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_hashig_pwd(self):
        u = User(id=1111,username='hariv20')
        u.set_password('hari_me')
        self.assertFalse(u.check_password('hari_you'))
        self.assertTrue(u.check_password('hari_me'))

    
    def test_update_streak(self):
        
        u1 = User(id=22222,username='peter',played = 0, win = 0, max_streak = 0, current_streak = 0, big_tree = 0, tree = 0, plant = 0,small_plant = 0, seed = 0)
        #u2 = User(id=33333,username='toby')
        g1 = Game(game_id=1111,user_id=22222,quiz_id=1,success=1,duration=85)
        #g2 = Game(game_id=1111,user_id=22222,quiz_id=2,success=1,duration=85)
        

        db.session.add(u1)
        db.session.add(g1)
        db.session.commit()
        

        user_id = u1.id
        data = {'user_id':22222, 'quizId':2,'success':1,'duration':85}
        #print(data)
        quizId = data['quizId']
        duration = data['duration']
        success = data['success']
        
        # Get user
        user = User.query.filter_by(id=user_id).first()
        #print(user)

        # Update number of game played by user
        user.played = user.played + 1


        if (success==True):
            user.win += 1

            if duration < 30:
                user.big_tree += 1
            elif duration <60:
                user.tree += 1
            elif duration <90:
                user.plant += 1
            elif duration < 120:
                user.small_plant += 1
            else:
                user.seed += 1
        
            # Update user's current_streak and max streak
            lastQuizWon = Game.query.filter(Game.user_id==user_id).filter(Game.success == True).order_by(Game.quiz_id.desc()).first()
            if lastQuizWon is not None:
                lastQuizId = lastQuizWon.quiz_id
                if quizId == lastQuizId + 1:
                    user.current_streak += 1
                else:
                    user.current_streak = 0
            else:
                user.current_streak += 1
        else:
            user.current_streak = 0
        if user.max_streak < user.current_streak:
            user.max_streak = user.current_streak
        
        
        
        
        
        self.assertTrue(user.current_streak,1)
        self.assertTrue(user.plant,1)








    
if __name__ == '__main__':
    unittest.main(verbosity=2)
