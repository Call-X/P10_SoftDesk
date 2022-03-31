from rest_framework import serializers
from core.models import CustomUser
from rest_framework_simplejwt.serializers import PasswordField, TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import AccessToken


class UserSerializer(serializers.ModelSerializer):
    
    password = PasswordField()
    class Meta(object):
        model = CustomUser
        fields = ['email','username', 'password']
        extra_kwards = {'password': {'write_only': True}}
        read_only_field = ['date_joined']
        
        def validate_password(self, password):
            if validate_password(password) is None:
                return make_password(password)
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # token = super().get_token(user)
        # token['username'] = user.username
        return AccessToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        access = self.get_token(self.user)
        data['access'] = str(access)
        return data