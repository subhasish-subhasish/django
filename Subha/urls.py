"""Subha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Subha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('photo/',views.photo,name='photo'),
    path('song/',views.song,name='song'),
    path('video/',views.video,name='video'),
    path("youtube/",views.youtube,name='youtube'),
    path("document/",views.document,name='document'),
    path('aboutus/',views.aboutus,name='aboutus')
]
