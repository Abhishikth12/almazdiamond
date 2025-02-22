from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.test_view, name='Homemain'),
    path('test2',views.test_2,name='test2'),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('admin_dashboard/ring-settings',views.ring_settings_admin,name='ring_settings_admin'),
    path('add-ring',views.add_edit_ring_settings,name='add_ring'),
    path('edit-ring/<int:id>',views.add_edit_ring_settings,name='edit_ring'),
    path('delete_ring_setting/<int:id>',views.delete_ring_setting,name='delete_ring_setting'),
    path('delete_ring_files/<int:rs_id>/<int:id>',views.delete_ring_files,name='delete_files'),
    path('delete_image/<int:rs_id>',views.delete_ring_files,name="delete_image"),
    path('login',views.login,name='login'),

]