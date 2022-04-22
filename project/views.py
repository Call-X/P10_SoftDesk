from re import I
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from core.models import CustomUser
from project.models import Contributor, Issues, Project, Comment
from project.serializers import ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status



class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        serializer = ProjectSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ProjectIssuesView(APIView):
    serializer_class = IssueSerializer
    queryset = Issues.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get(self, request, project_id=None):
        queryset = Issues.objects.filter(id=project_id)
        issues = get_object_or_404(queryset)
        self.check_object_permissions(request, issues)
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)
    
    #create
    def post(self, request, project_id=None):
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        serializer = IssueSerializer(data=request.data, context={'request': request, 'project': project_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectIssuesDetailView(APIView):
    serializer_class = IssueSerializer
    queryset = Issues.objects.all()
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, id=None, project_id=None):
        queryset = Issues.objects.filter(id=id, project=project_id)
        issue = get_object_or_404(queryset, id=id)
        serializer = IssueSerializer(issue)
        return Response(request, serializer.data)
    
    #update
    def put(self, request, id=None, project_id=None):
        queryset = Issues.objects.filter(id=id, project_id=project_id)
        issue = get_object_or_404(queryset, id=id)
        serializer = IssueSerializer(issue, data=request.data, context={'request': request, 'project': project_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, id=None, project_id=None):
        queryset = Issues.objects.filter(id=id, project=project_id)
        issue = get_object_or_404(queryset, id=id)
        comments  = Comment.objects.filter(issue=id)
        self.check_object_permissions(request, issue)
        issue.delete()
        for comment in comments:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
class ProjectCommentView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
   
    
    def get(self, request, project_id=None, issue_id=None):
        if not Issues.objects.filter(id=issue_id, project=project_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        queryset = Comment.objects.filter(issue_project=project_id, issue=issue_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, project_id=None, issue_id=None):
        if not Issues.objects.filter(id=issue_id, project=project_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        project = Project.objects.get(id=project_id) 
        self.check_object_permissions(request, project)     
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user, issue=Issues.objects.get(id=issue_id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    
class ProjectCommentDetailView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    
    def retrieve(self, request, project_id=None, issue_id=None):
        queryset = Comment.objects.filter(id=id, issue_project=project_id, issue=issue_id )
        comment = get_object_or_404(queryset, id=id)
        serializer = CommentSerializer(comment)
        self.check_object_permissions(request, comment)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, id=None, project_id=None, issue_id=None):
        if not Issues.objects.filter(id=issue_id, project=project_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment = get_object_or_404(Comment, id=id, issue=issue_id)
        self.check_object_permissions(request, comment)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user, issue=Issues.objects.get(id=issue_id))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, id=None, project_id=None, issue_id=None):
        if not Issues.objects.filter(id=issue_id, project=project_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment = get_object_or_404(Comment, id=id, issue=issue_id)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ContributorView(APIView):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, project_id=None):
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        if not Project.objects.filter(id=project_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = Contributor.objects.filter(project=project_id)
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, project_id=None):
        project = get_object_or_404(Project, id=project_id)
        self.check_object_permissions(request, project)
        serializer = ContributorSerializer(data=request.data, context={'request': request, 'project': project_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContributorDetailView(APIView): 
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, id=None, project_id=None):
        # project = get_object_or_404(Project, id=project_id)
        # self.check_object_permissions(request, project)
        # if not Project.objects.filter(id=project_id).exists():
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        
        queryset = Contributor.objects.filter(id=id, project=project_id)
        contributor = get_object_or_404(queryset, id=id)
        self.check_object_permissions(request, contributor)
        contributor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
    
    
    
            
        
        
    