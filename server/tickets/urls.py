from django.urls import path
from .views import bookTicket

app_name = 'ticket'

urlpatterns = [
    path('bookticket/', bookTicket, name='bookTicket'),
    path('bookticket/<int:locationID>', bookTicket, name='bookTicket'),
]
