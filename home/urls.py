from django.urls import path
from . import views

urlpatterns = [
    path('loginpage', views.loginpage, name='loginpage'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    
    path('', views.home, name='home'),
    path('categories', views.categories, name='categories'),
    path('vehicles', views.vehicles, name='vehicles'),
    path('car_detail/<str:pk_test>/', views.carDetail, name='car_detail'),
    path('vehiclebooking', views.vehiclebooking, name='vehiclebooking'),
    path('admindashboard', views.adminDashboard, name='admindashboard'),
]
