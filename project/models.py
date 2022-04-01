from django.conf import settings
from django.db import models

TYPE_CHOICE = [
    ('project', 'project'),
    ('product', 'product'),
    ('application', 'application')
]

PERMISSION_CHOICES = [
    ('manager', 'Manager'),
    ('contributeur', 'Contributeur'),
]

PRIORITY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low') 
]

TAG_CHOICES = [
    ('task', 'Task'),
    ('glitch', 'Glitch'),
    ('improvement', 'Improvement')
]

class Project(models.Model):
    title = models.CharField(max_length=138)
    description = models.TextField(max_length=3000)
    project_type = models.CharField(choices=TYPE_CHOICE, max_length=138)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, related_name='contributors', on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSION_CHOICES, max_length=128)
    role = models.CharField(max_length=128)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['user', 'project'], name='unique_user'),
            ]
        
class Issues(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(choices=TAG_CHOICES, max_length=128)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=128)
    project_id = models.ForeignKey(to='Project', related_name='issues', on_delete=models.CASCADE)
    status = models.CharField(max_length=128)
    autor_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='assgnee', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    
    
class Comments(models.Model):
    description = models.TextField(max_length=3000)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issues, related_name='comment', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    