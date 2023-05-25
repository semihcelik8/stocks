from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to="img/%Y")
    date = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    iden = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
