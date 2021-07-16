from django import views
from django.urls import path

from contacts.views.inquiry import Inquiry

app_name = 'contacts'

urlpatterns = [
    path('inquiry', Inquiry.as_view(), name='inquiry'),
]
