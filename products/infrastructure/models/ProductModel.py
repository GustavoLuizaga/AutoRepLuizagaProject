from django.db import models
from products.infrastructure.models.BrandModel import BrandModel

class ProductModel(models.Model):
    stock = models.IntegerField(default=0)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    reorder= models.IntegerField(default=0)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)