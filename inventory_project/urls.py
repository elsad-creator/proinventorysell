from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('prosellbase/', admin.site.urls),
    path('', include('inventory.urls')),  # inventory tətbiqinin URL-ləri
]