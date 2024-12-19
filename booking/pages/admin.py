from django.contrib import admin
from .models import CoffeeOrder

# Register your models here.
class pagesadmin(admin.ModelAdmin):
    pass

admin.site.register(CoffeeOrder, pagesadmin)