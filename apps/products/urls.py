from django.urls import path
from apps.products import views

app_name = "products"

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('product_detail', views.ProductDetail.as_view(), name='product_detail'),
    path('product_create', views.ProductCreate.as_view(), name='product_create'),
    path('product_update', views.ProductUpdate.as_view(), name='product_update'),
    path('product_delete', views.ProductDelete.as_view(), name='product_delete'),
]