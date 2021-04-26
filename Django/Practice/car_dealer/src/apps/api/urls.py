from django.urls import path

from .views import LoginAPIView, LogoutAPIView, CarAPIView, OrderAPIView, DealerCarsAPIView, CarCreateApi, CarUpdateApi, \
    CarDeleteApi, CarPublishAPI

app_name = 'api'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api_login'),
    path('logout/', LogoutAPIView.as_view(), name='api_logout'),
    path('cars/', CarAPIView.as_view(), name='car_api'),
    path('mycars/', DealerCarsAPIView.as_view(), name='dealer_cars_api'),
    path('mycars/create/', CarCreateApi.as_view(), name='car_create_api'),
    path('mycars/<int:pk>/update/', CarUpdateApi.as_view(), name='car_update_api'),
    path('mycars/<int:pk>/delete/', CarDeleteApi.as_view(), name='car_delete_api'),

    path('mycars/<int:pk>/publish/', CarPublishAPI.as_view({'post': 'publish'}), name='car_publish_api'),
    path('mycars/<int:pk>/unpublish/', CarPublishAPI.as_view({'post': 'unpublish'}), name='car_unpublish_api'),

    path('order/', OrderAPIView.as_view(), name='order_api'),
]

