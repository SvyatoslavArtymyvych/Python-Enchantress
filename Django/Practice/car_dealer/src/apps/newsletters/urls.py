from django.urls import path

from .views import NewsLetterView, SuccessfulView

app_name = 'newsletters'

urlpatterns = [
    path('', NewsLetterView.as_view(), name='newsletters-subscribe'),
    path('successful/', SuccessfulView.as_view(), name='newsletters-subscribe'),
]

