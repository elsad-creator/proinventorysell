from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'product_name', 'date_added', 'added_by')  # Admin panelində göstəriləcək sütunlar
    search_fields = ('serial_number', 'product_name', 'added_by__username')  # Axtarış funksionallığı
    list_filter = ('date_added', 'added_by')  # Filtirləmə funksionallığı

admin.site.register(Product, ProductAdmin)