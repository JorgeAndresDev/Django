from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView# Asegúrate de crear el modelo Product en models.py
from django.urls import reverse_lazy

# Vista para listar todos los usuarios
class UsertList(TemplateView):
    template_name = 'users/user_list.html'

# Vista para crear un nuevo usuario  
class UsertForm(TemplateView):
    template_name = 'users/user_form.html'