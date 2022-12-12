from django.shortcuts import render
from django.contrib import messages
from users.models import User
from rest_framework.decorators import api_view
from users.models import User
from .models import Location
from rest_framework.response import Response
from .serializer import LocationSerializers
# from rest_framework.response import Response
# from .forms import locationForm
# Create your views here.

# /api/location


@api_view(['GET', 'POST'])
def newLocation(request):
    if request.method == "POST":
        name = request.POST.get('locationName')
        address = request.POST.get('locationAddress')
        description = request.POST.get('locationDescription')
        adminusername = request.POST.get('locationAdmin')
        adminFlag = User.objects.filter(username=adminusername).exists()
        if (adminFlag == False):
            messages.error(
                request, "The username provided does not exist. Please enter correct UserName.")
            return render(request, 'users/locationform.html')
        else:
            admin = User.objects.get(username=adminusername)
            images = request.FILES.get('locationImg')
            try:
                status = request.POST['locationStatus']
                print("status ", status)
            except:
                status = False
                print("status ", status)

            newlocation = Location(name=name, address=address,
                                   description=description, admin=admin, images=images, status=status)
            newlocation.save()

            messages.success(
                request, "Location details have been submitted. We will verify and get back on the email of the Admin.")
            return render(request, 'locationform.html')

    else:
        return render(request, 'locationform.html')


@api_view(['GET'])
def getLocations(request):
    locations = Location.objects.all()
    data = LocationSerializers(locations, many=True).data
    return Response({
        'locations': data
    })
