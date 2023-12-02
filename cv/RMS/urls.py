from http.client import HTTPResponse
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from . import views



urlpatterns = [
    
               path('',views.home, name="home" ),
               
               path('login',views.login, name="login" ),
               
               path('logout',views.logout, name="logout" ),

               path('department',views.department, name="department" ),

               
               path('userprofile',views.userprofile, name="userprofile" ),
               
               path('companyprofile',views.companyprofile, name="companyprofile" ),
               
               path('register',views.register, name="register" ),

               path('about',views.about, name="about" ),
               
               path('noti',views.noti, name="noti" ),

] 