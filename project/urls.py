from django.urls import path
from project.views import ProjectViewset, ProjectIssuesView, ProjectCommentView, ContributorView, ProjectIssuesDetailView, ContributorDetailView, ProjectCommentDetailView


create_project = ProjectViewset.as_view({
     'get': 'list',
     'post': 'create'
 })

detail_project = ProjectViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
 })

urlpatterns = ([
    path('create_project/', create_project, name='project'),
    path('projects/<int:pk>/', detail_project, name='detail_project'),
    path('projects/<int:project_id>/issues/', ProjectIssuesView.as_view()),
    path('projects/<int:project_id>/issues/<int:id>/', ProjectIssuesDetailView.as_view()),
    path('projects/<int:project_id>/issues/<int:issue_id>/comments/', ProjectCommentView.as_view()),
    path('projects/<int:project_id>/issues/<int:issue_id>/comments/<int:id>/', ProjectCommentDetailView.as_view()),
    path('projects/<int:project_id>/contributors/', ContributorView.as_view()),
    path('projects/<int:project_id>/contributors/<int:id>/', ContributorDetailView.as_view()),
   
    

 ])









