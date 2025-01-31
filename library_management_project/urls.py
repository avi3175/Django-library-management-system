from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('ebooks/', include('books.urls')),
    path('freebooks/', include('free_books.urls')),
    path("cart/", include("cart.urls")),
    path('api-auth/', include('rest_framework.urls')),
]




