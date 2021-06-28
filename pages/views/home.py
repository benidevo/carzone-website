from django.shortcuts import render
from django.views import View
from database.models.teams import Team
from database.models.cars import Car

class Home(View):

    def get(self, request):
        teams = Team.objects.all()
        all_cars = Car.objects.all()
        featured_cars = Car.objects.filter(is_featured=True)
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()

        context = {
            'teams': teams,
            'featured_cars': featured_cars,
            'all_cars': all_cars,
            'model_search': model_search,
            'city_search': city_search,
            'body_style_search': body_style_search,
            'year_search': year_search
        }
        
        return render(request, 'pages/home.html', context)