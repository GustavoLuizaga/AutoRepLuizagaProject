from django.db import models

class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    countryOrigin = models.CharField(max_length=100)

