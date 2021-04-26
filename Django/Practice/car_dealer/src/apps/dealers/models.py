from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.country.name} | {self.name}'


class Dealer(AbstractUser):
    title = models.CharField(max_length=25)
    email = models.CharField(max_length=30, unique=True)
    city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title