from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from database.models.contact import Contact
from django.core.mail import send_mail

class Inquiry(View):

    def post(self, request):
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_state = request.POST['customer_state']
        customer_city = request.POST['customer_city']
        customer_need = request.POST['customer_need']
        customer_email = request.POST['customer_email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Contact.objects.filter(car_id=car_id, user_id=user_id)
            if has_inquired:
                messages.error(request, 'You have already made an inquiry')
                return redirect('/cars/'+car_id)
       
        contact = Contact(car_id=car_id, car_name=car_name, user_id=user_id, first_name=first_name, last_name=last_name, customer_state=customer_state, customer_city=customer_city, customer_need=customer_need, customer_email=customer_email, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New Car Inquiry',
            f'You have a new car inquiry for {car_name} from {first_name} {last_name}. Please login to your admin panel to view the notification',
            'benidevoo@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your request has been submitted we will contact you shortly')
        return redirect('/cars/'+car_id)