from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.

def home(request):
	return render(request, 'home.html', {'name': 'Edder'})

def inventory(request):
	searchTerm = request.GET.get('searchProduct')
	
	if searchTerm:
		products = Product.objects.filter(name__icontains=searchTerm)
	else:
		products = Product.objects.all()

	return render(request, 'inventory.html', {'searchTerm': searchTerm, 'products': products})