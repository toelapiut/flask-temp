import unittest
from app,models import User

class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(password='bananass')

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not True)