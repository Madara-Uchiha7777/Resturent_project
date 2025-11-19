from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Booking 
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Message from {name}"
        full_message = f"Sender Email: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,  # sender email (your configured Gmail)
            ['jayastalin7777@gmail.com'],  # receiver email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


 # ✅ import your model

def booktable(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')

        # ✅ Save booking data into the database
        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            message=message
        )

        return HttpResponse("✅ Your table has been booked successfully!")

    return render(request, 'bookingtable.html')

