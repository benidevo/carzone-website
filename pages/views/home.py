from django.shortcuts import render
from django.views import View
from database.models.teams import Team

class Home(View):

    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'pages/home.html', {'teams': teams})