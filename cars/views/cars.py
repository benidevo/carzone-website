from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from database.models.cars import Car


class Cars(View):

    def get(self, request):
        cars = Car.objects.all()
        paginator = Paginator(cars, 4)
        page = request.GET.get('page')
        paged_cars = paginator.get_page(page)
        context = {'cars': paged_cars}
        return render(request, 'cars/cars.html', context)