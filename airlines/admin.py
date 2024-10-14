from django.contrib import admin

# Register your models here.
from .models import Airline, Aircraft


admin.site.register(Airline)
admin.site.register(Aircraft)
