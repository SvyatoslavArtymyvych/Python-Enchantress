from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.IntegerField(unique=True)


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country_id = models.ForeignKey(to=Country, on_delete=models.CASCADE, null=True)


class Dealer(AbstractUser):
    title = models.CharField(max_length=25)
    email = models.CharField(max_length=30, unique=True)
    city_id = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True)
