from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import CountryCreateForm, CountriesList

app_name = 'dealers'

urlpatterns = [
    path('create/', CountryCreateForm.as_view(), name='country-create'),
    path('', CountriesList.as_view(), name='countries-list'),
]

