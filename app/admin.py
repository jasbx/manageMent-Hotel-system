from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Employess)
admin.site.register(Customers)
admin.site.register(Reservations)
admin.site.register(Meals)

