from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.test_view, name='test'),
    path('test2',views.test_2,name='test2'),
]