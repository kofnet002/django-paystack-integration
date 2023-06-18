from django.urls import path
from .views import initiate_payment,verify_payment


urlpatterns = [
    path('', initiate_payment, name='payment'),
    path('verify-payment/<str:ref>/', verify_payment, name='verify-payment'),
]