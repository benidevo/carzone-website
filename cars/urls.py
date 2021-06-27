from django.urls import path

from cars.views.cars import Cars
from cars.views.car_details import CarDetails
app_name = 'cars'

urlpatterns = [
    path('', Cars.as_view(), name='cars'), 
    path('<int:id>', CarDetails.as_view(), name='car-details'),
]
