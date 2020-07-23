"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path, include
from django.views.generic import ListView
from .models import Register
from . import views

urlpatterns = [
    re_path(r'^$', ListView.as_view(queryset=Register.objects.all().order_by("-birthdate")[:25], template_name="registro/home.html")),
    re_path(r'^new/$', views.newregister, name='registers')
]
