from django.urls import path
from .views import completePayment

app_name = 'payment'
urlpatterns = [
    path('paymentstatus/', completePayment, name='completePayment'),
]
