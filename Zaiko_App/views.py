from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
	return render(request, 'home.html')

def inventory(request):
	searchTerm = request.GET.get('searchProduct')
	if searchTerm:
		products = Product.objects.filter(name__icontains=searchTerm)
	else:
		products = Product.objects.all()
	
	contexto = {'searchTerm': searchTerm, 
				'products': products}

	return render(request, 'inventory.html', contexto)

def create_product(request):
	if request.method == 'POST': 
		producto = Product()
		producto.name = request.POST.get('txtName')
		producto.description = request.POST.get('txtDescription')
		producto.amount = request.POST.get('txtAmount')
		producto.price = request.POST.get('txtPrice')
		producto.code = request.POST.get('txtCode')
		producto.image = request.FILES.get('txtImagen')

		if producto.image != None:
			producto.save()

	return render(request, 'create.html')

def delete(request):
	searchTerm = request.GET.get('searchProduct')

	if searchTerm:
		products = Product.objects.get(code = searchTerm)
		products.delete()
		
	return render(request, 'delete.html', {'searchTerm': searchTerm})

def sell(request):
	searchTerm = request.GET.get('searchProduct')
	cantidad = request.GET.get('cantidad')

	if searchTerm and cantidad:
		cantidad = int(cantidad)
		products = Product.objects.get(code = searchTerm)
		products.amount -= cantidad
		products.save()
		
	return render(request, 'sell.html', {'searchTerm': searchTerm, 'cantidad': cantidad})


