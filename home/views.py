from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import CarFilter

# Create your views here.


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('admindashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admindashboard')

        return render(request, 'home/login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

def home(request):
    return render(request, 'home/home.html')

def vehicles(request):
    cars = Car.objects.all()
    total_cars = cars.count()
    myFilter = CarFilter(request.GET, queryset=cars)
    cars = myFilter.qs

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

    
    

    context = {'cars':cars, 'total_cars':total_cars, 'myFilter':myFilter}
    return render(request, 'home/vehicles.html', context)


def services(request):
    return render(request, 'home/services.html')

def carDetail(request, pk_test):
    car = Car.objects.get(id=pk_test)
    context = {'car':car}
    return render(request, 'home/cardetails.html', context)

def vehiclebooking(request):
    caar = Car.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        datefrom_str = request.POST.get('datefrom')
        dateto_str = request.POST.get('dateto')

        date_from = datetime.strptime(datefrom_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        date_to = datetime.strptime(dateto_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        car_type_name = request.POST.get('carType')
        car_instance = Car.objects.get(name=car_type_name)
        message = request.POST.get('message')
        booking = Booking(firstname=firstname, lastname=lastname, email=email, phoneno=phone, date_from=date_from, date_to=date_to, car_type=car_instance, message=message )
        booking.save()


    context = {'caar':caar,}

    return render(request, 'home/vehiclebooking.html', context)

@login_required(login_url='loginpage')
def adminDashboard(request):
    bookings = Booking.objects.all()

    context = {'bookings':bookings}
    return render(request, 'home/admindashboard.html', context)


