"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from firstapp import views
from firstapp import models
import firstapp.models as m
import firstapp.views as fv
from . import views as cv


urlpatterns = [
    path("admin/", admin.site.urls),
    path('index1/', fv.index1),
    path('index2/', fv.index2),
    path('first/', include('firstapp.urls')),
    path('second/', include('secondapp.urls')),
    path('home/', cv.home),
    path('text/<str:ccc>', cv.text),
    path('',cv.home),
    path('/', cv.home),
    path('file/', include('file.urls')),
]
