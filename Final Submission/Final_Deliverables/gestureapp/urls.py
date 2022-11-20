from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('work/',views.handle,name='handle'),
]
