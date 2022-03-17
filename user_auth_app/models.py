from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


# Create your models here.
class UserProfileInfo(models.Model):
    DOCTOR = 1
    PATIENT = 0
    ROLE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    )
    role = models.PositiveIntegerField(choices=ROLE_CHOICES,blank=True, null=True)
    # here we are using default user and default user already have name, email, password
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    # aditional classes                                                                        
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    address_line1 = models.TextField(max_length=200)
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)              
    address_pincode = models.IntegerField()
    def __str__(self) -> str:                                                                 
        return self.user.username           # username is a default attribute from this User  

