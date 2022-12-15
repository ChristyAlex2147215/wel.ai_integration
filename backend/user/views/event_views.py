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



@api_view(['GET'])
def getEvents(request):
    events=Events.objects.all()
    serializer=EventSerializer(events,many=True)
    print(serializer.data)
    return Response(serializer.data)


  


@api_view(['GET'])
def getEvent(request,pk):
    # event=None
    # for i in events.events:
    #     if i['_id']==pk:#becouse the pk l
    #         event=i
    #         break
    events=Events.objects.get(id=int(pk))
    serializer=EventSerializer(events,many=False)
    print(serializer.data)
    return Response(serializer.data)