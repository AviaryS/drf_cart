from django.contrib import admin
from django.urls import path

from cart_app.views import CartAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', CartAPIView.as_view()),
    path('cart/<int:pk>/', CartAPIView.as_view()),
]
