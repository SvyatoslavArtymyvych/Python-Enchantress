from django.contrib import admin

# Register your models here.
from apps.newsletters.models import NewsLetter


@admin.register(NewsLetter)
class CityAdminModel(admin.ModelAdmin):
    search_fields = ('email', )