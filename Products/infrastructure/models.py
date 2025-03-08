from django.db import models

class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    countryOrigin = models.CharField(max_length=100)

class Product(models.Model):
    stock = models.IntegerField(default=0)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=200)
    reorder= models.IntegerField(default=0)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
