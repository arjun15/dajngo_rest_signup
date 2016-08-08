"""
importing allowany from rest_framework,
 user model ,
serializer from signup app
"""
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView)

from signup.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """
    creating user
    """
    model = User
    queryset = User.objects.all()
    permisson_class = (AllowAny,)
    serializer_class = UserSerializer


class UserList(ListAPIView):
    """
    to show user list
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    """
    to display individual details of a user
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(DestroyAPIView):
    """
    to delete a particular user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    """
    updates the user details
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
