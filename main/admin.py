from django.contrib import admin

# Register your models here.
from main.models import Product
admin.site.site_header = "Sitio web de inventarios"
admin.site.site_title = "Portal de inventarios"
admin.site.index_title = "Bienvenidos al portal de administración"


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit_price']
    search_fields = ['name', 'quantity']
    list_filter = ['name', 'unit_price']

admin.site.register(Product, ProductoAdmin)