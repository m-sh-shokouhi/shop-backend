"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from cart.api.v1 import views as cart_views
from products.api.v1 import views as products_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', products_views.CategoryViewSet)
router.register(r'products', products_views.ProductViewSet)
router.register(r'product-images', products_views.ProductImageViewSet)
router.register(r'carts', cart_views.CartViewSet)
router.register(r'cart-items', cart_views.CartItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
