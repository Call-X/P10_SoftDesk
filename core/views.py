from rest_framework.generics import CreateAPIView
from core.models import CustomUser
from core.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()