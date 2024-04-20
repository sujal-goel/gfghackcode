from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customuser(AbstractUser):
    c=(("s","standard"),("a","artist"),("o","organisation"))
    c1=(("m","Male"),("f","female"))
    username=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=100,default="")
    age=models.IntegerField(default=0,blank=True)
    occupation=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=10,choices=c1,default="m",blank=True)
    phone=models.CharField(max_length=100,default="",blank=True)
    user_type= models.CharField(max_length=30,choices=c,default="",blank=True)
    user_bio=models.CharField(max_length=200,default="",blank=True)
    user_profile_image=models.ImageField(upload_to='static/user_images', default='static/user_images/person.svg',blank=True)

    def __str__(self):
        return self.username
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

class image(models.Model):
    name = models.CharField(max_length=250)
    cover_pic = models.FileField(upload_to="media/%Y/%m/%d")
    artist=models.TextField()
    category=models.TextField()
    decription = models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name