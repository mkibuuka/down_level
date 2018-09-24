from unittest import TestCase
from core.accounts import User


class TestUserAccounts(TestCase):
    """
    Test class for testing individual user accounts
    """
    def setUp(self):
        self.new_user = User('michael', 'mic@me.com', 'thisisapassword')

    def test_create_user(self):

        self.assertEqual(self.new_user.username, 'michael')
        self.assertEqual(self.new_user.email, 'mic@me.com')
        self.assertEqual(self.new_user.password, 'thisisapassword')

    def test_insert_user_account(self):
        User.add_account(self.new_user.username, self.new_user.email, self.new_user.password)
        self.assertEqual(len(User.accounts), 1)

    def test_user_login_successful(self):
        self.assertTrue(User.login(self.new_user.username))

    def test_user_login_unsuccessful(self):
        User.login('Ivan')
        self.assertRaises(KeyError)
