from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
User = get_user_model()
# Create your views here.
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        type=request.POST.get('type')
        pass1 = request.POST.get("psw")
        pass2 = request.POST.get("psw2")

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password mismatched")
        else:
            my_user=User.objects.create(uname=uname,email=email,password=pass1,user_type=type)
            return redirect('home')
    return render(request,"sign.html")
