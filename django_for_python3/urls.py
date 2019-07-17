"""django_for_python3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include
from captcha import urls
from django.urls import path
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', login_views.index),
    path(r'index/', login_views.index),
    path(r'login/', login_views.login),
    path(r'register/', login_views.register),
    path(r'logout/', login_views.logout),
    path(r'captcha/', include('captcha.urls'))
]
