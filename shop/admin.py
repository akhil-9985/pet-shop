from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem, Category

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)