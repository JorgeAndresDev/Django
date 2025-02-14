from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product  # Asegúrate de crear el modelo Product en models.py
from django.urls import reverse_lazy

# Vista para listar todos los productos
class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

# Vista para ver los detalles de un producto
class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

# Vista para crear un nuevo producto
class ProductCreate(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price']  # Campos del modelo Product
    success_url = reverse_lazy('products:product_list')

# Vista para actualizar un producto existente
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('products:product_list')

# Vista para eliminar un producto
class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')

