from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


# Create your models here.
class UserProfileInfo(models.Model):
    # here we are using default user and default user already have name, email, password
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    # aditional classes                                                                        
    portfolio_site = models.URLField(blank=True)                                               
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)                  
    def __str__(self) -> str:                                                                 
        return self.user.username           # username is a default attribute from this User  

