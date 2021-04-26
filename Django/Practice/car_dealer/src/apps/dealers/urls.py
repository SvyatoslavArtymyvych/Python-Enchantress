from django.urls import path

from .views import CountryCreateForm, CountriesList, LoginView, RegisterView, logout_view

app_name = 'dealers'

urlpatterns = [
    path('countries/create/', CountryCreateForm.as_view(), name='country-create'),
    path('countries/', CountriesList.as_view(), name='countries-list'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('logout/', logout_view, name='logout-page'),
]

