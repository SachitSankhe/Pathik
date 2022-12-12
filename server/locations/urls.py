
from django.urls import path
from locations.views import newLocation, getLocations

app_name = 'locations'
urlpatterns = [
    path('', getLocations),
    path('addlocation/', newLocation, name='newLocation'),
]
