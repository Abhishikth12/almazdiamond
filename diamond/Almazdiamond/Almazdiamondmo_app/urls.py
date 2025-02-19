from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.test_view, name='Homemain'),
    path('test2',views.test_2,name='test2'),
    path('login',views.login,name='login'),
]