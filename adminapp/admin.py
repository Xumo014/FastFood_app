from django.contrib import admin

from food.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderProduct)