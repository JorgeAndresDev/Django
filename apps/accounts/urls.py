from django.urls import path
from apps.accounts import views
from django.views.generic.base import RedirectView

app_name = "accounts"

urlpatterns = [
    path('', RedirectView.as_view(url='login')),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.LogOut.as_view(), name='logout')
]