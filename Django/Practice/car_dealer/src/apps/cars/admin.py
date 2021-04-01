from django.contrib import admin

# Register your models here.
from apps.cars.models import Model, Color, Brand, Car, Property, CarProperty, Picture, Order

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Property)
admin.site.register(CarProperty)
admin.site.register(Picture)
admin.site.register(Order)
