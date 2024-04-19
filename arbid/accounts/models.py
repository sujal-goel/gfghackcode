from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customuser(AbstractUser):
    username=models.CharField(max_length=30,unique=True)
    phone=models.CharField(max_length=100,unique=True)
    user_type= models.CharField(max_length=30)
    user_bio=models.CharField(max_length=200)
    user_profile_image=models.ImageField(upload_to="profile")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []