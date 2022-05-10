import unittest
from app.models import User
from app import db, email


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='ray',password='123rnk', email = 'rachael.kiarie@student.moringaschool.com')

    #tests if the password is hashed and that it's not an empty value
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password
    
    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('123rnk'))
    def tearDown(self):
        User.query.delete()