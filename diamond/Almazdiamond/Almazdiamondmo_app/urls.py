from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.test_view, name='Homemain'),
    path('test2',views.test_2,name='test2'),

    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('submitproduct',views.submit_product,name="submitproduct"),

    path('setting',views.setting,name="setting"),
    path('stone',views.stone,name="stone"),



    path('login',views.login,name='login'),

]