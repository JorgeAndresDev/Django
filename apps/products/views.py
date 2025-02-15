from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView# Asegúrate de crear el modelo Product en models.py
from django.urls import reverse_lazy

# Vista para listar todos los productos
class ProductList(TemplateView):
    template_name = 'products/product_list.html'

# Vista para crear un nuevo producto
class Productform(TemplateView):
    template_name = 'products/product_form.html'

