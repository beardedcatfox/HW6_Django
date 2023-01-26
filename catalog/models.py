from django.db import models


class City(models.Model):
    name = models.CharField(max_length=119)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=119)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=119)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Retailer(models.Model):
    name = models.CharField(max_length=255)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
