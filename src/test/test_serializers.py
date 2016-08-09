"""
test all serializer.py file content
"""
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase


class TestUser(APITestCase):
    """
    create user using serializer.py file
    """

    def setUp(self):
        """
        setup a new user
        """
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword')

    def test_can_read_user_list(self):
        """
        User list checked using get method
        """
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        """
        read specific user infomation
        """
        response = self.client.get('/user/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_validate_password(self):
        """
        validate password
        """

        response = self.client.post("http://127.0.0.1:8000/register/",
                                    {
                                        'username': 'ajs123',
                                        'email': 'a@gmail.com',
                                        'password': 'qwe',
                                        'confirm_password': 'qwerty',
                                        'mobile_number': '+918149888748'})
        self.assertEqual(response.status_code, 400)

    def test_validate_confirm_password(self):
        """
        validate confirm password
        """

        response = self.client.post("http://127.0.0.1:8000/register/",
                                    {
                                        'username': 'ajs12345',
                                        'email': 'a@gmail.com',
                                        'password': 'amazatic',
                                        'confirm_password': 'ama',
                                        'mobile_number': '+918149888748'})
        self.assertEqual(response.status_code, 400)

    def test_validate(self):
        """
        Check two password match or not
        """

        response = self.client.post("http://127.0.0.1:8000/register/",
                                    {
                                        'username': 'ajs123789',
                                        'email': 'a@gmail.com',
                                        'password': 'amazatic',
                                        'confirm_password': '1234567',
                                        'mobile_number': '+918149888748'})
        self.assertEqual(response.status_code, 400)
