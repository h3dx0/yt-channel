from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from main.forms import ProductForm
from main.models import Product


@login_required
def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products':page_obj
    }
    return  render(request, 'listado_productos.html', context=context)

def create_product(request):
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product-created')
    context = {
       'form': form
    }
    return  render(request, 'create_product.html', context=context)

def product_created(request):
    return render(request, 'product-created.html')