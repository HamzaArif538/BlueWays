from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def vehicles(request):
    cars = Car.objects.all()
    context = {'cars':cars}
    return render(request, 'home/vehicles.html', context)


def categories(request):
    return render(request, 'home/categories.html')