from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    outcityprice = models.IntegerField(null=True)
    car_model = models.CharField(max_length=4 ,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    picture = models.ImageField(upload_to='car_pictures/', null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    TRANSMITION = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    )
    transmition = models.CharField(max_length=200, null=True, choices=TRANSMITION)
    CATEGORY = (
        ('SUV', 'SUV'),
        ('Luxury', 'Luxury'),
        ('Economy', 'Economy'),
        ('Executive', 'Executive'),
    )
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return f"{self.manufacturer} {self.name}"
    

class Booking(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.EmailField(("Email"), max_length=254, null=True)
    phoneno = models.CharField(max_length=13, null=True)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)
    car_type = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    message = models.TextField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

