from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages, auth

class Register(View):

    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('users:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                    return redirect('users:register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, 'You are now logged in')
                    return redirect('users:dashboard')
                   
            
        else:
            messages.error(request,'passwords do not match')
            return redirect('users:register')
            