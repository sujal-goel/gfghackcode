from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login

User = get_user_model()
# Create your views here.
def home(request):
    return HttpResponse("this is the home page")
