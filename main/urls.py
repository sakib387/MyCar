
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.lending_page,name="main"),
    path('home',views.home_view,name="home"),
    path('list',views.list_view,name='list')
]
