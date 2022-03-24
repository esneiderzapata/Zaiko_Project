from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'home.html', {'name': 'Edder'})

def inventory(request):
	searchTerm = request.GET.get('searchProduct')
	return render(request, 'inventory.html', {'searchTerm': searchTerm})