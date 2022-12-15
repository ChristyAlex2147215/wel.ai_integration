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

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/user/<id>',
        '/api/user/create',
        '/api/user/events',
        '/api/user/events/<id>'
        '/api/user/events/create',
        '/api/user/events/update',
        '/api/user/events/delete'

    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user=request.user #from the token takes the user details
    serializer=UserSerializer(user,many=False)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    print(serializer.data)
    return Response(serializer.data)  


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


@api_view(['POST'])
def registerUser(request):
    data=request.data
    try:
        user =User.objects.create(
            first_name=data["name"],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
            )
        serializer=UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message={"detail":"User with this email already exist"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


