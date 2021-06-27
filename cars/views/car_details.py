from django.shortcuts import render, get_object_or_404
from django.views import View
from database.models.cars import Car

class CarDetails(View):

    def get(self, request, id):
        car = get_object_or_404(Car, pk=id)
        context = {'car': car}
        return render(request, 'cars/car_details.html', context)