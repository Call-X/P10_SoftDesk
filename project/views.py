from project.models import Contributor, Issues, Project, Comment
from project.permissions import IsProjectManager, IsProjectManagerUser, IsProjectContributor
from project.serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status

class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsProjectManager]

    def create(self, request):
        serializer = ProjectSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProjectIssuesView(ListCreateAPIView):
    serializer_class = IssueSerializer
    queryset = Issues.objects.all()
    permission_classes = [IsAuthenticated, IsProjectContributor]
    
    def get_queryset(self, *args, **kwargs):  
        return Issues.objects.filter(project_id=self.kwargs.get('project_id'))
class ProjectIssuesDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = IssueSerializer
    queryset = Issues.objects.all()
    permission_classes = [IsAuthenticated, IsProjectContributor]
    lookup_field = 'id'
    
    def get_queryset(self, *args, **kwargs):
        return Issues.objects.filter(project_id=self.kwargs.get('project_id'))

class ProjectCommentView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]
    queryset = Comment.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(issue_id=self.kwargs.get('issue_id'))
    
class ProjectCommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]
    queryset = Comment.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(issue_id=self.kwargs.get('issue_id'))

class ContributorView(ListCreateAPIView):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectManagerUser]
    queryset = Contributor.objects.all()
    
    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs.get('project_id'))
    
    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(project_id=Contributor.objects.get(id=self.kwargs.get('project_id')), user_id=self.request.user)
class ContributorDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectManagerUser]
    lookup_field = 'id'
    
    def get_queryset(self, *args, **kwargs):
        return Contributor.objects.filter(project_id=self.kwargs.get('project_id'))