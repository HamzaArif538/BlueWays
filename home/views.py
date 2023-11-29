from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def vehicles(request):
    cars = Car.objects.all()
    total_cars = cars.count()

    sort_option  = request.GET.get('sort', None)

    if sort_option == 'price_low':
        cars = cars.order_by('price')
    elif sort_option == 'price_high':
        cars = cars.order_by('-price')
    elif sort_option == 'name_asc':
        cars = cars.order_by('manufacturer')
    elif sort_option == 'name_desc':
        cars = cars.order_by('-manufacturer')
    elif sort_option == 'latest':
        cars = cars.order_by('-date_created')

    page = request.GET.get('page', 1)
    paginator = Paginator(cars, 15)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)


    context = {'cars':cars, 'total_cars':total_cars}
    return render(request, 'home/vehicles.html', context)


def categories(request):
    return render(request, 'home/categories.html')