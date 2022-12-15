from django.shortcuts import render
from django.http import JsonResponse #gives json responses
from . import events
from rest_framework.response import Response #rest responses 
from rest_framework.decorators import api_view,permission_classes #rest access method 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from .models import Events,User
from .serializer import EventSerializer #serializing data
from .serializer import UserSerializer, UserSerializerWithToken
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status #to respond with error messages when the user registers with an already existing email

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        # data["username"]=self.user.username
        # data["email"]=self.user.email

        serializer=UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]=v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer