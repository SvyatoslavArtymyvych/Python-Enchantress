from django.contrib import admin

# Register your models here.
from apps.cars.models import Model, Color, Brand, Car, Property, CarProperty, Picture, Order
from django.utils.safestring import mark_safe


@admin.register(Color)
class ColorAdminModel(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Brand)
class BrandAdminModel(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Model)
class ModelAdminModel(admin.ModelAdmin):
    search_fields = ('brand', 'name')
    autocomplete_fields = ('brand', )
    list_filter = ('brand', )
    list_display = ('brand', 'name')


@admin.register(Car)
class CarAdminModel(admin.ModelAdmin):
    search_fields = ('model', 'dealer')
    autocomplete_fields = ('model', 'dealer',)
    list_filter = ('color', 'dealer', 'fuel_type', 'status', )
    list_display = ('dealer', 'model', 'color', 'engine_type', 'fuel_type', 'price',)


@admin.register(Property)
class PropertyAdminModel(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category', )
    list_display = ('name', 'category',)


@admin.register(CarProperty)
class CarPropertyAdminModel(admin.ModelAdmin):
    search_fields = ('car', )
    autocomplete_fields = ('property', 'car',)
    list_filter = ('property',)
    list_display = ('car', 'property',)


@admin.register(Picture)
class PictureAdminModel(admin.ModelAdmin):
    search_fields = ('car', )
    autocomplete_fields = ('car',)
    list_filter = ('car',)
    list_display = ('car', 'position', 'metadata',)


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    search_fields = ('car', )
    autocomplete_fields = ('car',)
    list_filter = ('status',)
    list_display = ('car', 'status', 'message',)
