from django.contrib import admin
from .models import Booking

class bookingdmin(admin.ModelAdmin):
    pass


admin.site.register(Booking, bookingdmin)
