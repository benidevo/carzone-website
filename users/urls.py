from django import views
from django.urls import path

from users.views.login import Login
from users.views.dashboard import Dashboard
from users.views.register import Register
from users.views.logout import Logout

app_name = 'users'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('logout', Logout.as_view(), name='logout'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
]
