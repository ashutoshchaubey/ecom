from django.contrib import admin
from .models import Profile, Products, Blouse, Shirts, Skirts, Gowns, Cart, Specifications, Content, Order, OrderItem
# Register your models here.
admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(Blouse)
admin.site.register(Shirts)
admin.site.register(Skirts)
admin.site.register(Gowns)
admin.site.register(Cart)
admin.site.register(Specifications)
admin.site.register(Content)
admin.site.register(Order)
admin.site.register(OrderItem)