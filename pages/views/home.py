from django.shortcuts import render
from django.views import View
from database.models.teams import Team
from database.models.cars import Car

class Home(View):

    def get(self, request):
        teams = Team.objects.all()
        all_cars = Car.objects.all()
        featured_cars = Car.objects.filter(is_featured=True)
        context = {
            'teams': teams,
            'featured_cars': featured_cars,
            'all_cars': all_cars
        }
        return render(request, 'pages/home.html', context)