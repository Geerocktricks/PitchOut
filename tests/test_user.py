import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self):
        '''
        set up will run before every test
        '''
        self.new_user = User(id = 1, username = "geerocktricks", email = "geerocktricks.com", password_hash = "hashed_password")
    def tearDown(self):
        '''
        test case to check if new instance is created
        '''
        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()
        
    # def test_instance(self):
    #     '''
    #     test case to check if new instance is created
    #     '''
    #     self.assertTrue(isinstance(self.new_user, User))

    # def test_password_setter(self):
    #     '''
    #     test to check if password is being hashed
    #     '''
    #     self.assertTrue(self.new_user.password_hash is not None)


    # def test_check_instance(self):
    #     '''
    #     test case to check if new instance is created
    #     '''
    #     self.assertEquals(self.new_pitch.pitch_title,'Pitch')
    #     self.assertEquals(self.new_pitch.pitch_content,'Pitch content')
    #     self.assertEquals(self.new_pitch.category,"pickup")

    # def test_save_pitch(self):
    #     '''
    #     test case to check if new instance is saved
    #     '''
    #     self.new_pitch.save_pitch()
    #     self.assertTrue(len(Pitch.query.all()) > 0)

    # def test_get_pitch_by_id(self):
    #     self.new_pitch.save_pitch()
    #     pitch = Pitch.get_pitch(123)
    #     self.assertTrue(pitch is not None)
