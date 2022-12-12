from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
from locations.models import Location
from .serializers import TicketSerializer
from .models import Ticket
from django.conf import settings

# Create your views here.
from instamojo_wrapper import Instamojo


@api_view(['GET', 'POST'])
def bookTicket(request):
    if request.method == "POST":
        data = ({
            'user': User.objects.get(username=request.POST.get('user')).pk,
            'location': Location.objects.get(name=request.POST.get('location')).pk,
            'date': request.POST.get('date'),
            'quantity': request.POST.get('quantity'),
            'amount': request.POST.get('amount'),
        })
        ticket = TicketSerializer(data=data)
        if ticket.is_valid():
            # ticket.save()
            # Getting all the items from the frontend after validation
            user = User.objects.get(username=request.POST.get('user'))
            location = Location.objects.get(name=request.POST.get('location'))
            date = request.POST.get('date')
            quantity = request.POST.get('quantity')
            amount = request.POST.get('amount')

            # Creating Instamojo Client and Order id
            client = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN,
                               endpoint='https://test.instamojo.com/api/1.1/')

            payment_response = client.payment_request_create(
                amount=amount,
                purpose='Buying a ticket',
                buyer_name=user.username,
                email=user.email,
                send_email=True,
                redirect_url='http://localhost:8000/api/payment/paymentstatus/'
            )
            print(payment_response)
            order_id = payment_response['payment_request']['id']
            tempTicket = Ticket.objects.get_or_create(user=user, location=location,
                                                      date=date, quantity=quantity, amount=amount, payment_id=order_id)

            return render(request, 'payment.html', {'payment_url': payment_response['payment_request']['longurl']})

        return Response(ticket.errors)
    else:
        location = Location.objects.get(request.GET.get("locationID"))
        if location is None:
            return render(request, 'form.html')
        else:
            return render(request, 'form.html', {"locationName": location.name})
