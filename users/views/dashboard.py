from django.shortcuts import render
from django.views import View

class Dashboard(View):

    def get(self, request):
        return render(request, 'users/dashboard.html')