from django.db import models
from users.models import User
from locations.models import Location
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    quantity = models.IntegerField(default=1, null=False, validators=[
        MaxValueValidator(6),
        MinValueValidator(1)
    ]
    )
    amount = models.IntegerField(default=0)
    payment_id = models.CharField(
        max_length=100, default='sbcsndicjasidnckasbndckasndciuj')
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return (str(self.id)+"_"+self.user.username+"_"+self.location.name+"_"+str(self.paid))
