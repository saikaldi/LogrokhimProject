from django.db import models
from django.conf import settings
from catalog.models import Product

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукты")

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.email} - {self.product.name}"

    class Meta:
        verbose_name = 'Избранные'
        verbose_name_plural = 'Избранные'
