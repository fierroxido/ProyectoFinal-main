from django.contrib import admin
from django.urls import path
from . import views 
from django.urls import include

urlpatterns = [
    path('accounts/', views.registro),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registro/', views.registro, name="registro"),
]
