from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from database.models.cars import Car


class Cars(View):

    def get(self, request):
        cars = Car.objects.order_by('-added_at')
        paginator = Paginator(cars, 4)
        page = request.GET.get('page')
        paged_cars = paginator.get_page(page)
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        
        context = {
            'cars': paged_cars,
            'model_search': model_search,
            'city_search': city_search,
            'body_style_search': body_style_search,
            'year_search': year_search
        }
        return render(request, 'cars/cars.html', context)