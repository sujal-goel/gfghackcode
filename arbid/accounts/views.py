from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        user_type = request.POST.get('type')
        pass1 = request.POST.get("psw")
        pass2 = request.POST.get("psw2")

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password mismatched")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)

            my_user.phone = phone
            my_user.name = phone
            my_user.user_type = user_type
            my_user.save()

            return redirect('home')

    return render(request, "sign.html")

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('psw')
        user = authenticate(request, username=uname, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Your password and confirm password mismatched")
            
    return render(request, 'login.html')

def profile_settings(request):
    return render(request,"setting.html")