from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
def home(request):
    # dic={}
    # if User is not None:
    #     username= request.user.username
    #     pic=request.user.user_profile_image
    #     dic['username']=username
    #     dic['pic']=pic
    return render(request,"index.html")
def explore(request):
    return render(request,"explore.html")