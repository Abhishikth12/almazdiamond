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
    path('admin_dashboard/ring-settings-variant/<int:ring_id>',views.ring_setting_variant_admin,name='ring_settings_variant_admin'),
    path('add-ring-variant/<int:ring_id>',views.add_edit_ring_setting_variant,name='add_ring_variant'),
    path('edit-ring-variant/<int:ring_id>/<int:id>',views.add_edit_ring_setting_variant,name='edit_ring_variant'),
    path('delete_ring_setting_variant/<int:ring_id>/<int:id>',views.delete_ring_setting_variant,name='delete_ring_setting_variant'),

    path('delete_ring_files/<int:rs_id>/<int:id>',views.delete_ring_files,name='delete_files'),
    path('delete_image/<int:rs_id>',views.delete_ring_files,name="delete_image"),
    path('login',views.login,name='login'),
    path('admin_dashboard/stone',views.stone_admin,name='stone_admin'),
    path('add-stone',views.add_edit_stone,name='add_stone'),
    path('edit-stone/<int:id>',views.add_edit_stone,name='edit_stone'),
    path('delete_stone/<int:id>',views.delete_stone,name='delete_stone'),
    path('delete_stone_files/<int:s_id>/<int:id>',views.delete_stone_files,name='delete_stone_files'),
    path('delete_stone_image/<int:s_id>',views.delete_stone_files,name="delete_stone_image"),
    path('ring_stone_combination_admin',views.ring_stone_combination_admin,name='ring_stone_combination_admin'),
    path('add-combination',views.add_edit_combination,name="add_combination"),
    path('edit-combination<int:id>',views.add_edit_combination,name='edit_combination'),
    path('delete-combination/<int:id>',views.delete_combination,name='delete_combination'),
    path('delete_combination_files/<int:c_id>/<int:id>',views.delete_combination_files,name='delete_combination_files'),
    path('ring-settings',views.ring_settings,name='ring_settings'),
    path('ring-details/<int:id>',views.get_more_ring_details,name="get_more_ring_details"),
    path('ring-settings/<int:stone_id>',views.ring_settings,name='stone_ring_settings'),
    path('ring-details/<int:id>/<int:stone_id>',views.get_more_ring_details,name="stone_get_more_ring_details"),
    path('stone-ring-setting/<int:stone_id>/<int:ring_id>',views.combination_stone_ring,name='combination_stone_ring'),
    path('stone',views.stones,name='stone'),
    path('stone/<int:ring_id>',views.stones,name='ring_setting_stone'),
    path('stone-details/<int:id>/<int:ring_id>',views.get_more_stone_details,name="ring_get_more_stone_details"),
    path('stone-details/<int:id>',views.get_more_stone_details,name="get_more_stone_details"),
    path('serach_ring_details',views.get_more_ring_details,name='serach_ring_details'),
    path('serach_ring_details/<int:stone_id>',views.get_more_ring_details,name='serach_ring_details'),
    
    path('serach_stones',views.stones,name='serach_stones'),
    path('addto_wishlist',views.addto_wishlist,name='addto_wishlist'),
    path('addto_cart',views.addto_cart,name='addto_cart'),
    path('view_wishlist',views.view_wishlist,name="view_wishlist"),
    path('view_cart',views.view_cart,name="view_cart"),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),
    # path('api/ring_setting_filter_api',views.ring_setting_filter_api,name='ring_setting_filter_api'),
]