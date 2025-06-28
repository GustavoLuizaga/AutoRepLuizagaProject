from django.db import models
from .ProductModel import ProductModel

class ImageProductModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images_product')
    image_url = models.CharField(max_length=250)
