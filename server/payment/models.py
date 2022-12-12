from django.db import models
from tickets.models import Ticket

# Create your models here.


class Payment(models.Model):
    payment_request_id = models.CharField(max_length=150)
    payment_id = models.CharField(max_length=150)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    response = models.TextField(max_length=1000)
