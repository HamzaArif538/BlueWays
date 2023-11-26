from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def vehicles(request):
    return render(request, 'home/vehicles.html')


def categories(request):
    return render(request, 'home/categories.html')