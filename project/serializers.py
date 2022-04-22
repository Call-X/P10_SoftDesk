from email.policy import default
from django.forms import ValidationError
from rest_framework import serializers
from core.models import CustomUser
from project.models import Contributor, Issues, Project, Comment
from rest_framework.validators import UniqueTogetherValidator

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']
        
class ContributorSerializer(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.all()
    )
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'permission', 'role']
        
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(),
                fields=['project', 'user']                    
                )
            ]
        
class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        issue_id = serializers.ReadOnlyField(source='id')
        author =  serializers.ReadOnlyField(source='author.username')
        assignee = serializers.SlugRelatedField(                                  
            queryset=CustomUser.objects.all(),
            slug_field='username',
            default=serializers.CurrentUserDefault()
            )
        
        model = Issues
        fields = [
                'id', 
                'title', 
                'desc', 
                'tag', 
                'priority', 
                'project_id', 
                'status', 
                'author', 
                'assignee', 
                'create_time'
                ]
    def validate_assignee(self, assignee):
        user_id = CustomUser.objects.get(username=assignee).id
        if not Contributor.objects.filter(
            user=user_id, project=self.context['project']).exists():
            error_message = 'The assignee'\
                            + str(assignee)\
                            + 'is not register for the project.'
            raise serializers.ValidationError(error_message)
        return assignee       

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = [
                'description',
                'author',
                'issue'
                'create_time'
                ]
        
        
        
        
