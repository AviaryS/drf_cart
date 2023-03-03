from django.contrib import admin

from cart_app.models import Product, Cart

admin.site.register(Product)
admin.site.register(Cart)