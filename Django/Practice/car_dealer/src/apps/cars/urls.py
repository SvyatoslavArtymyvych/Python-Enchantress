from django.urls import path

from .views import ShowCars, CarDetails, OrderView

app_name = 'cars'

urlpatterns = [
    path('', ShowCars.as_view(), name='car-creation'),
    path('<int:car_id>/', CarDetails.as_view(), name='car-detail'),
    path('<int:car_id>/order/', OrderView.as_view(), name='order-page'),
]

