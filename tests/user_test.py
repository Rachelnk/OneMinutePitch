# from turtle import title
# from unicodedata import category
import unittest
from app.models import User, Pitch, Comment
from app import db, email


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='ray',password='123rnk', email = 'rachael.kiarie@student.moringaschool.com')

    def test_instance_user(self):
        '''
        Tests the instances of user
        '''
        self.assertEquals(self.new_user, User) 
      
    #tests if the password is hashed and that it's not an empty value
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password
    
    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('123rnk'))

class PitchTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch= Pitch( title='Open water ATM', category = 'business idea', user_id = 'ray')
        
    def test_instance(self):
        '''
        Tests the instances of pitch
        '''
        self.assertEquals(self.new_pitch, Pitch)

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.new_comment= Comment( comment ='Good idea', pitch_id = 'first pitch', user_id = 'ray')
        
    def test_instance(self):
        '''
        Tests the instances of Comment
        '''
        self.assertEquals(self.new_comment, Comment)
       
    def tearDown(self):
        User.query.delete()
        Comment.query.delete()
        Pitch.query.delete()
if __name__ == '__main__':
    unittest.main()