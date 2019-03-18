from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar_chef/', views.buscar_chef, name='buscar_chef'),
    path('checkout/', views.checkout, name='checkout')
]