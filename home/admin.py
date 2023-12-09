from django.contrib import admin


# Register your models here.

from .models import *
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Booking)
admin.site.register(Contact)