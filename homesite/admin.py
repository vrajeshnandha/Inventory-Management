from django.contrib import admin
from .models import Fabric, Cutting, StockEntry

# Register your models here.

admin.site.register(Fabric)
admin.site.register(Cutting)
admin.site.register(StockEntry)
