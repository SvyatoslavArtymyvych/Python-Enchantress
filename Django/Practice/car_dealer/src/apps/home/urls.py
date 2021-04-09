from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import home_page, HomePage

app_name = 'home'

urlpatterns = [
    path('', HomePage.as_view(), name='main-page'),
]

