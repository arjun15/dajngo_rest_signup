"""
These file do following task
1. Check user created apis
"""
from django.test import TestCase


class TestUser(TestCase):
    """
    Valid Data
    """

    def test_add_view(self):
        """
        test views.py file
        """
        response = self.client.post("http://127.0.0.1:8000/register/",
                                    {
                                        'username': 'ajs',
                                        'email': 'a@gmail.com',
                                        'password': 'qwerty',
                                        'confirm_password': 'qwerty',
                                        'mobile_number': '+918149888748'})

        self.assertEqual(response.status_code, 201)
        response = self.client.post("http://127.0.0.1:8000/register/",
                                    {
                                        'username': 'ajs',
                                        'email': 'a@gmail.com',
                                        'password': 'qwerty',
                                        'confirm_password': 'qwerty',
                                        'mobile_number': ' + 918149888748'})
        self.assertEqual(response.status_code, 400)

        response = self.client.get("http://127.0.0.1:8000/user/1/")
        print(response.content)
