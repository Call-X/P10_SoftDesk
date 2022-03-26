from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        if not email:
            raise ValueError('the given email must be set')
        email=self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(email, password=password, **extra_fields)
        
                
class CustomUser(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=128, unique=True)
    date_joined = models.DateTimeField(auto_now=True)
    type = models
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name']
