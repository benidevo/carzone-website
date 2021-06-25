from django.urls import path

from cars.views.cars import Cars

app_name = 'cars'

urlpatterns = [
    path('', Cars.as_view(), name='cars'), 
]
