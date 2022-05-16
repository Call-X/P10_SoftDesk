from rest_framework import serializers
from core.models import CustomUser
from project.models import Contributor, Issues, Project, Comment
from rest_framework.validators import UniqueTogetherValidator
from django_currentuser.middleware import get_current_authenticated_user
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
                fields=['user', 'project'],
            ),
        ]
        
class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        issues_id = serializers.ReadOnlyField(source='id')
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
                'project', 
                'status', 
                'author', 
                'assignee', 
                'create_time'
                ]
        
    def validate(self, data):
        if not Contributor.objects.filter(
                    user=data['assignee'], project=data['project']).exists():
            error_message = 'The assignee '\
                            + str(data['assignee'])\
                            + ' is not registered for the project.'
            raise serializers.ValidationError(error_message)
        return super().validate(data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
                'description',
                'author',
                'issue',
                'create_time'
                ]
        read_only_fields = ['author']
        
    def create(self, validated_data):
    
        validated_data['author']=get_current_authenticated_user()
        comment= Comment.objects.create(**validated_data)
        return comment
