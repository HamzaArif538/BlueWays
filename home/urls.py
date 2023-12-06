from django.urls import path
from . import views

urlpatterns = [
    path('loginpage', views.loginpage, name='loginpage'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    
    path('', views.home, name='home'),
    
    path('vehicles', views.vehicles, name='vehicles'),
    path('car_detail/<str:pk_test>/', views.carDetail, name='car_detail'),
    path('vehiclebooking', views.vehiclebooking, name='vehiclebooking'),
    path('admindashboard', views.adminDashboard, name='admindashboard'),

    path('services', views.services, name='services'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
]
