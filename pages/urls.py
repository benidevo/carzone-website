from django import views
from django.urls import path

from pages.views.home import Home
from pages.views.about import About
from pages.views.cars import Cars
from pages.views.services import Services
from pages.views.contact import Contact

app_name = 'pages'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('services', Services.as_view(), name='services'),
    # path('cars', Cars.as_view(), name='cars'),
    path('contact', Contact.as_view(), name='contact'),
]
