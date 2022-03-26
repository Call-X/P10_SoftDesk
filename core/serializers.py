from rest_framework import serializers
from core.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ('id', 'last_name', 'first_name', 'email', 'password', 'username', 'date_joined')
        extra_kwards = {'password': {'write_only': True}}
        read_only_field = ['date_joined']