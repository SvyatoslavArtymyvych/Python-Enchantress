from django.contrib import admin

# Register your models here.
from apps.dealers.models import Country, City, Dealer


@admin.register(City)
class CityAdminModel(admin.ModelAdmin):
    search_fields = ('name', )
    autocomplete_fields = ('country',)


@admin.register(Country)
class CountryAdminModel(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Dealer)
class DealerAdminModel(admin.ModelAdmin):
    search_fields = ('title', )
    autocomplete_fields = ('city',)
    list_filter = ('city', )
    list_display = ('title', 'email', 'city')


