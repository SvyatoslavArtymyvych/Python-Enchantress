from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import CreateCarCreatingView, ShowCars, CarDetails

app_name = 'cars'

urlpatterns = [
    # path('create/', CreateCarCreatingView.as_view(), name='car-creation'),
    path('', ShowCars.as_view(), name='car-creation'),
    path('<int:car_id>/', CarDetails.as_view(), name='car-detail'),
]

