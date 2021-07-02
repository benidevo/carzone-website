from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from database.models.contact import Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

class Dashboard(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            inquiry = Contact.objects.order_by('-created_at').filter(user_id=request.user.id)
            context = {
                'inquiries': inquiry
            }
            return render(request, 'users/dashboard.html', context)
        else:
            messages.error(request, 'You need to be logged in to view the dashboard')
            return HttpResponseRedirect(reverse('users:login'))