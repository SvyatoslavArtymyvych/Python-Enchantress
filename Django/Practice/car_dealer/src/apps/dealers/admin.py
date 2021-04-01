from django.contrib import admin

# Register your models here.
from apps.dealers.models import Country, City, Dealer

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Dealer)
