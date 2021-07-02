from django.shortcuts import redirect
from django.contrib import messages, auth
from django.views import View

class Logout(View):

    def get(self, request):
        return redirect('pages:home')

    def post(self, request):
        auth.logout(request)
        return redirect('pages:home')