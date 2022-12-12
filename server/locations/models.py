from django.db import models
from users.models import User

# Create your models here.


def image_directory_path(instance, fileName):
    return 'locationImages/{0}/{1}/{2}'.format(instance.name, instance.admin.id, fileName)


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    address = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=150, null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=image_directory_path, max_length=100)
    status = models.BooleanField(null=False)

    def __str__(self) -> str:
        return self.name
