from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('categories', views.categories),
    path('vehicles', views.vehicles),
]
