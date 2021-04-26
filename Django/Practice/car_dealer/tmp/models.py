# This is an auto-generated Django model module.
from django.db import models


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    country_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'country'


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'city'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')

    class Meta:
        managed = False
        db_table = 'restaurant'


class Personnel(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, db_column='restaurant')

    class Meta:
        managed = False
        db_table = 'personnel'


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING, db_column='restaurant')

    class Meta:
        managed = False
        db_table = 'menu'


class Dish(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35)
    season = models.IntegerField()
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu')

    class Meta:
        managed = False
        db_table = 'dish'
