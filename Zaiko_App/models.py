from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	image = models.ImageField(upload_to='Zaiko_App/images/')
	amount = models.IntegerField()
	price = models.IntegerField()
	code = models.CharField(max_length=4)

	def __str__(self):
		return self.name

class ProductStats(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=4)
	amount = models.IntegerField()
	price = models.IntegerField()
	profit = models.IntegerField()

	def __str__(self):
		return self.name