from django.shortcuts import redirect
from django.contrib import messages, auth
from django.views import View

class Logout(View):

    def get(self, request):
        return redirect('pages:home')

    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have beesn successfully logged out.')
        return redirect('pages:home')