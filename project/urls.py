from django.urls import path
from project.views import CreateProjectAPIView

urlpatterns = [
    path("create/", CreateProjectAPIView.as_view()),
]