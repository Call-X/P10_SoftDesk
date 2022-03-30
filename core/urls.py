from django.urls import path
from core.views import CreateUserAPIView, MyObtainTokenPairView


urlpatterns = [
    path("register/", CreateUserAPIView.as_view()),
    path("login/", MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    
]
