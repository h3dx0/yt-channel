from django.urls import path
from main import views
app_name = 'main'
urlpatterns = [
    path('inicio', views.home, name='home'),
    path('create-product', views.create_product, name='create_product'),
    path('product-created', views.product_created, name='product_created'),
]