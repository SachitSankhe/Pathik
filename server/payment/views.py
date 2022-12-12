from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Payment
from django.http import HttpResponse
from tickets.models import Ticket
from instamojo_wrapper import Instamojo
from django.conf import settings
import cloudinary
import cloudinary.uploader
import cloudinary.api

from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

app_name = "payment"

# Completing the payment request,saving a Payment instance and sending a email with QR code


@api_view(['GET'])
def completePayment(request):
    payment_request_id = request.GET.get('payment_request_id')
    payment_status = request.GET.get('payment_status')
    payment_id = request.GET.get('payment_id')
    ticket = Ticket.objects.get(payment_id=payment_request_id)

    # Creating a client to verify payment request.
    client = Instamojo(api_key=settings.API_KEY,
                       auth_token=settings.AUTH_TOKEN,
                       endpoint='https://test.instamojo.com/api/1.1/')
    response = client.payment_request_payment_status(
        payment_request_id, payment_id)
    print(response)

    # Checking if payment has been successfully completed
    if (payment_status == 'Credit' and response['payment_request']['status'] == 'Completed'):
        ticket.paid = True
        ticket.save()
        payment = Payment(payment_request_id=payment_request_id,
                          payment_id=payment_id, ticket=ticket, response=response)
        payment.save()

        user = ticket.user

        config = cloudinary.config(secure=True)

        # Creating a payment response for QRcode
        payment_response = {
            'user_id': user.id,
            'ticket_id': ticket.id,
            'quantity': ticket.quantity,
            'order_id': payment_request_id,
            'payment_id': payment_id,
        }

        # Using a API for QR code generation
        link = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + \
            str(payment_response)
        # Sending a mail
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string(
            'confirmationEmail.html', {'date': ticket.date, 'location': ticket.location, 'link': link})

        send_mail("Confirmation email",
                  msg_plain,
                  settings.EMAIL_HOST_USER,
                  [user.email],
                  html_message=msg_html)

        #Rendering successfull payment page
        return render(request, 'success.html')
    else:
        return HttpResponse("Sone error occured. Payment not successful any money deducted will be refunded within 24hrs")
