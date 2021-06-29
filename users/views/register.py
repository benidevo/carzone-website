from django.shortcuts import render, redirect
from django.views import View

class Register(View):

    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        print('hello')
        return redirect('users:register')