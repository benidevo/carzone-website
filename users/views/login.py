from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.views import View

class Login(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('users:dashboard')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('users:login')