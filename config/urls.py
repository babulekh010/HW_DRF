
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('apps.account.urls')),
    path('api/v1/product/', include('apps.product.urls')),
    path('api/v1/category/', include('apps.category.urls')),
    path('api/v1/cart/', include('apps.cart.urls')),
]
