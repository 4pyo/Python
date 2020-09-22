from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
	path('' , views.home , name = 'Blog-home') ,
	path('about/<slug:slug>/' , views.about , name = 'about') ,
] 
