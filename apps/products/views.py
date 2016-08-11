from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Product


class ProductList(ListView):
    model = Product
    paginate_by = 10
    template_name = 'products/product_list.html'


class ProductDetail(DetailView):
    model = Product
