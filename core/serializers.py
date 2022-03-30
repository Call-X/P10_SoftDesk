from os import access
from rest_framework import serializers
from core.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ('id', 'last_name', 'first_name', 'email', 'password', 'username', 'date_joined')
        extra_kwards = {'password': {'write_only': True}}
        read_only_field = ['date_joined']
        
        def validate_passeword(self, value: str):
            return make_password(value)
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
     @classmethod
     def get_token(cls, user):
         return AccessToken.for_user(user)
     
     def validate(self, attrs):
         data = super().validate(attrs)
         access = self.get_token(self.user)
         data['access'] = str(access)
         return data
    
    # @classmethod
    # def get_token(cls, user):
    #     token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # # Add custom claims
        # token['username'] = user.username
        # return token