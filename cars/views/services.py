from django.shortcuts import render
from django.views import View

class Services(View):

    def get(self, request):
        return render(request, 'pages/services.html')