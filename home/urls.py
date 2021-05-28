from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('hacking', views.hacking, name='hacking'),
    path('programming', views.programming, name='programming'),
    path('resources', views.resources, name='resources'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
]

