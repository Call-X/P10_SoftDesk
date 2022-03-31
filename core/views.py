from urllib import request
from rest_framework.generics import CreateAPIView
from core.models import CustomUser
from core.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from core.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.response import Response
from rest_framework import status


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # queryset = CustomUser.objects.all()
class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer