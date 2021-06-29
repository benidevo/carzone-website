from django.shortcuts import render, redirect
from django.views import View

class Logout(View):

    def get(self, request):
        return redirect('pages:home')