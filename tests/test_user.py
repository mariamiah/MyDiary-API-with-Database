import unittest
from api.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(2, "mary", "maria@gmail.com", "1234")

    def test_user_id(self):
        # Tests that the user_id is equal to the given user_id
        self.assertEqual(self.user.user_id, 2, "user_id must be 1")
        self.user.user_id = 4
        self.assertEqual(self.user.user_id, 4, "user_id is now 4")

    def test_username(self):
        self.assertEqual(self.user.user_name, "mary")

    def test_email(self):
        self.assertEqual(self.user.email, "maria@gmail.com")
        self.user.email = "sandra@yahoo.com"
        self.assertEqual(self.user.email, "sandra@yahoo.com")

    def test_password(self):
        self.assertEqual(self.user.password, "1234")

    def test_class_instance(self):
        # Tests that the defined object is an instance of a class
        self.assertIsInstance(self.user, User)
