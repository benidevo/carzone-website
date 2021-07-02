from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from database.models.inquiries import Inquiry
from django.core.mail import send_mail


class Contact(View):

    def get(self, request):
        return render(request, 'pages/contact.html')

    def post(self, request):
        name = request.POST['name']
        email= request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = 'You have a new message from CarZone'
        message_body = f'Name: {name}\n Email: {email}\n Phone {phone}\n Message: {message}'

        send_mail(
            email_subject,
            message_body,
            'benidevoo@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        inquiry = Inquiry(name=name, email=email, message=message, subject=subject, phone=phone)
        inquiry.save()
        
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        return redirect('pages:contact')
