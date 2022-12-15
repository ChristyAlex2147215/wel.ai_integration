from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Events
from rest_framework_simplejwt.tokens import RefreshToken



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Events
        fields='__all__'  




class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    _id=serializers.SerializerMethodField(read_only=True)
    isAdmin=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= User
        fields=['username','email','id',"_id","name","isAdmin"]   


    def get_isAdmin(self,obj):
        return obj.is_staff
        
    def get__id(self,obj):
        return obj.id

    def get_name(self,obj):
        name=obj.first_name
        if name=="":
            name=obj.email
            # if name=="":
            #     name="No email"
        return name           



class UserSerializerWithToken(UserSerializer):#inherits UserSerializer from the same file to get variables _id,name,isAdmin
    token=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= User
        fields=['username','email','id',"_id","name","isAdmin","token"]   

    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)