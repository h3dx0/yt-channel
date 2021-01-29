from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = HTMLField(default="")
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"

    def __str__(self):
        return "{}".format(self.name)


