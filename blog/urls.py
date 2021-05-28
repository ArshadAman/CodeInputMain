from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome,name='blogHome'),
    path('None', views.Nones,name='None'),
    path('<str:slug>', views.blogPost,name='blogPost'),


]
