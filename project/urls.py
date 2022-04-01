from django.urls import path, include
from project.views import ProjectViewset
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('projects', ProjectViewset, basename='projects')

urlpatterns = [
    path("", include(router.urls))
]

# path("create_project/", ProjectViewset.as_view()),