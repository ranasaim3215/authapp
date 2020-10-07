
from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.admin_login, name='index'),
    path('home/', views.home, name='home')

]
