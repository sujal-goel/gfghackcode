"""
URL configuration for arbid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),
    path('signup/',signup,name="signup"),
    path('login_view/',login_view,name="login_view"),
    path('explore/',explore,name="explore"),
    path('community/',community,name="community"),
    path('settings/',profile_settings,name="profile_setting")


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
