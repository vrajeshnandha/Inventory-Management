from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Fabric)
admin.site.register(Cutting)
admin.site.register(StockEntry)
admin.site.register(Worker)
admin.site.register(Payment)
admin.site.register(Variance)
