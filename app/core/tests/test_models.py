from django.test import TestCase
from django.contrib.auth import get_user_model


# helper functions and constants
def get_email_password():
    """Helper function that returns the tuple of defaul email and password"""
    email = 'test@greatsoft.uz'
    password = 'password1234'
    return email, password


class ModelTest(TestCase):

    def test_user_create_with_email_successful(self):
        """Test that creating a new user with email is successful"""
        email, password = get_email_password()
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # checking part
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normilized(self):
        """Test the email for a new user is normilized"""
        email, password = get_email_password()
        email = 'test@GREATSOFT.UZ'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # checking part
        self.assertEqual(user.email, email.lower())

    def test_creating_user_with_no_email(self):
        """Test that creates user without email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpassword')

    def test_creating_super_user_successful(self):
        """Test that creates a superuser"""
        email, password = get_email_password()
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        # checking part
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

