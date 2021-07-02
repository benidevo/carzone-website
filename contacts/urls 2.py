from django import views
from django.urls import path

from contacts.views.inquiry import Inquiry
# from contacts.views.about import About
# from contacts.views.services import Services
# from contacts.views.contact import Contact

app_name = 'contacts'

urlpatterns = [
    path('inquiry', Inquiry.as_view(), name='inquiry'),
    # path('about', About.as_view(), name='about'),
    # path('services', Services.as_view(), name='services'),
    # path('contact', Contact.as_view(), name='contact'),
]
