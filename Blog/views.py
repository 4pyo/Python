from django.shortcuts import render
from .models import Product

def home (request):
	home = Product.objects.all()
	context = {
		'home' : home ,
	}
	return render (request , 'Blog/home.html' , context)

def about(request , slug):
	about = Product.objects.get(slug=slug)
	context = {
		'about':about ,
	}
	return render(request , 'Blog/about.html' , context)

