from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    serial_number = models.CharField(max_length=100, verbose_name="Serial Nömrəsi")
    product_name = models.CharField(max_length=200, verbose_name="Məhsul Adı")
    date_added = models.DateField(verbose_name="Əlavə Edilmə Tarixi")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Əlavə Edən")

    def __str__(self):
        return f"{self.product_name} ({self.serial_number})"

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"