from django.urls import path
from apps.products import views

app_name = "products"

urlpatterns = [
    path('product_list', views.ProductList.as_view(), name='product_list'),
    path('product_form', views.Productform.as_view(), name='product_form'),
]