"""
URL configuration for verst1 project.

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
from app import views

urlpatterns = [
    path('', views.indexNoRegister, name='start'),
    path('<int:page>', views.indexNoRegister, name='start'),
    path('register/<int:page>', views.indexRegister, name='startReg'),
    path('searchTag/<tag><int:page>', views.serchTag, name='search'),
    path('searchTagR/<tag><int:page>', views.serchTagR, name='searchReg'),
    path('register', views.register, name='register'),
    path('register/error', views.registerError, name='registerError'),
    path('register/question/<int:question_id>', views.question, name='question'),
    path('register/ask', views.ask, name='ask'),
    path('register/ask/error', views.errorAsk, name='errorAsk'),
    path('register/settings', views.settings, name='settings'),
    path('register/settings/error', views.settingsError, name='settingsError'),
    path('login', views.logIn, name='logIn'),
    path('login/error', views.errorLogIn, name='errorLogIn'),
    path('admin/', admin.site.urls),
]
