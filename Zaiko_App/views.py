from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Product
from .models import ProductStats
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

		productostats = ProductStats()
		productostats.name = request.POST.get('txtName')
		productostats.code = request.POST.get('txtCode')
		productostats.price = request.POST.get('txtPrice')
		productostats.amount = 0
		productostats.profit = 0

		if producto.image != None:
			productostats.save()
			producto.save()
			return redirect('inventory')

	return render(request, 'create.html')

def delete(request):
	searchTerm = request.GET.get('searchProduct')

	if searchTerm:
		products = Product.objects.get(code = searchTerm)
		stats = ProductStats.objects.get(code = searchTerm)
		products.delete()
		stats.delete()
		
	return render(request, 'delete.html', {'searchTerm': searchTerm})

def sell(request):
	productsA = Product.objects.all()
	codes=[]
	amounts=[]
	codexamount = str(request.GET.get('CC')).split()

	if len(codexamount)>=2:
		for i in range(0,len(codexamount)):
			if i%2==0:
				codes.append(codexamount[i])
			else:
				amounts.append(int(codexamount[i]))

		for i in range(0,len(codes)):
			products = Product.objects.get(code = codes[i])
			jorge = ProductStats.objects.get(code = codes[i])

			products.amount -= amounts[i]
			products.save()

			jorge.amount += amounts[i]
			jorge.profit = jorge.amount*jorge.price
			jorge.save()
		
	return render(request, 'sell.html', {'productsA':productsA})

def stats(request):
	productsA = ProductStats.objects.all()

	masVendido = ['','',-1]
	menosVendido = ['','',999999999999]

	masGanancias = ['','',-1]
	menosGanancias = ['','',999999999999]

	gananciasTotales = 0

	for x in productsA:
		if(x.amount > masVendido[2]):
			masVendido[0] = x.name
			masVendido[1] = x.code
			masVendido[2] = x.amount

		if(x.profit > masGanancias[2]):
			masGanancias[0] = x.name
			masGanancias[1] = x.code
			masGanancias[2] = x.profit

		if(x.amount < menosVendido[2]):
			menosVendido[0] = x.name
			menosVendido[1] = x.code
			menosVendido[2] = x.amount

		if(x.profit < menosGanancias[2]):
			menosGanancias[0] = x.name
			menosGanancias[1] = x.code
			menosGanancias[2] = x.profit

		gananciasTotales += x.profit

	contexto = {'productsA':productsA,'masVendido':masVendido,'masGanancias':masGanancias,'menosVendido':menosVendido,'menosGanancias':menosGanancias,'gananciasTotales':gananciasTotales}
		
	return render(request, 'stats.html', contexto)

def end(request):
	productsA = ProductStats.objects.all()

	for x in productsA:
		x.amount = 0
		x.profit = 0
		x.save()
		
	return redirect('inventory')

