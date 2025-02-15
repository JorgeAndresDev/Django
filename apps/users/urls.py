from django.urls import path
from apps.users import views

app_name = "users"

urlpatterns = [
    path('user_list', views.UsertList.as_view(), name='user_list'),
    path('user_form', views.UsertForm.as_view(), name='user_form'),
]