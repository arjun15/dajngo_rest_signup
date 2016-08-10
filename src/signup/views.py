"""
importing allowany from rest_framework,
 user model ,
serializer from signup app
"""
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView)
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from signup.permissions import IsOwnerOrReadOnly
from signup.serializers import (
    UserSerializer, UpdateSerializer, MyPhotoSerializer)
from signup.models import MyPhoto


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


class UserUpdate(UpdateAPIView):
    """
    updates the user details
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UpdateSerializer


class PhotoList(CreateAPIView):
    model = MyPhoto
    queryset = MyPhoto.objects.all()
    serializer_class = MyPhotoSerializer

    # def post(self, request, format=None):
    #     serializer = MyPhotoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
