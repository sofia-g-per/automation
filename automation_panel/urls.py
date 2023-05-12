from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/host', views.createHost, name="create-host"),
    path('delete/hosts', views.deleteHosts, name="delete-hosts"),
]    
