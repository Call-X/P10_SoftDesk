from django.urls import path
from core.views import CreateUserAPIView

urlpatterns = [
    path("create/", CreateUserAPIView.as_view()),
]
