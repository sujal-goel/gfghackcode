from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.models import *
User = get_user_model()
# Create your views here.
def home(request):
    images=image.objects.all()
    return render(request,"index.html",{"images":images,"value":1})
def explore(request):
    images=image.objects.all()

    return render(request,"explore.html",{"images":images})
def community(request):
    return render(request,"community.html")