from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    price = models.IntegerField()