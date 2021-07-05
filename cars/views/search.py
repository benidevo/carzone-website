from django.shortcuts import render
from django.views import View

from database.models.cars import Car

class Search(View):

    def get(self, request):
        cars = Car.objects.all()
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
        
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                cars = Car.objects.filter(name__icontains=keyword)

        if 'model' in request.GET:
            model = request.GET['model']
            if model:
                cars = Car.objects.filter(model__iexact=model)

        if 'year' in request.GET:
            year = request.GET['year']
            if year:
                cars = Car.objects.filter(year__iexact=year)
        
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                cars = Car.objects.filter(city__iexact=city)

        if 'body_style' in request.GET:
            body_style = request.GET['body_style']
            if body_style:
                cars = Car.objects.filter(body_style__iexact=body_style)
        
        if 'transmission' in request.GET:
            transmission =request.GET['transmission']
            if transmission:
                cars = Car.objects.filter(transmission__iexact=transmission)
        
        if 'min_price' in request.GET:
            min_price = request.GET['min_price']
            max_price = request.GET['max_price']
            if max_price:
                cars = Car.objects.filter(price__gte=min_price, price__lte=max_price)
            

        context = {
            'cars': cars,
            'model_search': model_search,
            'city_search': city_search,
            'body_style_search': body_style_search,
            'year_search': year_search,
            'transmission_search': transmission_search
        }
        return render(request, 'cars/search.html', context)