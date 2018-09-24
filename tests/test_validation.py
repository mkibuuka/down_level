from unittest import TestCase
from core.validation import validate_user_signup
from core.validation import validate_user_login
from core.accounts import User


class TestSignUpValidation(TestCase):
    """
    Test class to run test cases on validation functions

    """
    def setUp(self):
        self.user = User('michael', 'mycovan@gmail.com', '1234validation')
        self.user_1 = User('michael', 'myco.com', '1234validation')

    def test_user_sign_up_successful(self):
        response = validate_user_signup(self.user.username, self.user.email, self.user.password)
        self.assertTrue(response)

    def test_user_sign_up_unsuccessful_with_invalid_username(self):
        response = validate_user_signup("  ", self.user.email, self.user.password)
        self.assertEqual(response, 'Please provide a username')

    def test_user_sign_up_unsuccessful_with_invalid_email(self):
        response = validate_user_signup(self.user_1.username, self.user_1.email, self.user_1.password)
        self.assertEqual(response, 'invalid email or missing email address')

    def test_user_sign_up_unsuccessful_with_invalid_password(self):
        response = validate_user_signup(self.user.username, self.user.email, '1234')
        self.assertEqual(response, 'missing password/password should be atleast 8 characters')


class TestLoginValidation(TestCase):
    """
    Test class to run test cases on validation functions

    """
    def test_user_login_successful(self):
        response = validate_user_login('michael', '1234validation')
        self.assertTrue(response)

    def test_user_login_unsuccessful_with_invalid_username(self):
        response = validate_user_login('', '1234validation')
        self.assertEqual(response, 'Please provide a username')

    def test_user_login_unsuccessful_with_invalid_password(self):
        response = validate_user_login('michael', '12valid')
        self.assertEqual(response, 'missing password/password should be atleast 8 characters')
