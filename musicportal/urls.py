from django.contrib import admin
from django.urls import path
from .views import HomePage,Register,Login,logoutuser,Show



urlpatterns=[
    path('upload',HomePage,name='home-page'),
    path('',Register,name='register-page'),
    path('login/',Login,name='login-page'),
    path('logout/',logoutuser,name='logout'),
    path('show/',Show,name='show-page')
]
