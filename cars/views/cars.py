from django.shortcuts import render
from django.views import View

class Cars(View):

    def get(self, request):
        return render(request, 'cars/cars.html')