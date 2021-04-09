from django.db import models

from .choises import ORDER_STATUS_CHOICES, POPULATIONS_TYPES_CHOICES, FUEL_TYPE_CHOICES, STATUS_CHOICES, STATUS_NEW, \
    ORDER_STATUS_OPEN


# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand_id = models.ForeignKey(to=Brand, on_delete=models.PROTECT)
    name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    color_id = models.ForeignKey(to=Color, on_delete=models.PROTECT)
    dealer_id = models.ForeignKey(to='dealers.Dealer', on_delete=models.CASCADE, db_index=True)
    model_id = models.ForeignKey(to=Model, on_delete=models.DO_NOTHING, db_index=True)
    engine_type = models.CharField(max_length=20)
    population_type = models.CharField(max_length=1, choices=POPULATIONS_TYPES_CHOICES)
    price = models.FloatField()
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPE_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_NEW)
    doors = models.IntegerField()
    capacity = models.FloatField()
    gear_case = models.CharField(max_length=25)
    number = models.CharField(max_length=15)
    slug = models.CharField(max_length=20)
    sitting_place = models.IntegerField(default=2)
    first_registration_date = models.DateTimeField()
    engine_power = models.FloatField()

    def __str__(self):
        return f'{self.dealer_id.title} | {self.model_id.name} | {self.color_id.name}'


class Property(models.Model):
    category = models.CharField(max_length=35)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarProperty(models.Model):
    property_id = models.ForeignKey(to=Property, on_delete=models.CASCADE)
    car_id = models.ForeignKey(to=Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_id.model_id.name} | {self.property_id.name}'


class Picture(models.Model):
    car_id = models.ForeignKey(to=Car, on_delete=models.CASCADE, related_name='photos')
    url = models.ImageField(verbose_name="Car photo", null=True, blank=True)
    position = models.CharField(max_length=30)
    metadata = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.car_id.model_id.name} | {self.metadata}'


class Order(models.Model):
    car_id = models.ForeignKey(to=Car, on_delete=models.SET('Sold'))
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_OPEN)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=255)

    def __str__(self):
        return f'Status:{self.status} | {self.first_name} {self.last_name}'
