from django.contrib import admin
from .models import Delivery,Status,Product,Payments

# Register your models here.

admin.site.register(Delivery)
admin.site.register(Status)
admin.site.register(Product)
admin.site.register(Payments)
