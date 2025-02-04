from django.urls import path
from .views import *
urlpatterns = [
    path('', home_dashboard, name = 'home_dashboard'),
    path('login/', login_page, name = 'login_page'),
    path('logout/', logout_page, name = 'logout_page'),


    path('category/list/', category_list, name='category_list'),
    path('category/create/', category_add, name='create_category'),
    path('category/<int:pk>/edit', category_edit, name='edit_category'),
    path('category/<int:pk>/delete/',delete_category, name='delete_category'),

    path('product/list/', product_list, name='product_list'),
    path('product/create/', product_add, name='create_product'),
    path('product/<int:pk>/edit', product_edit, name='edit_product'),
    path('product/<int:pk>/delete/', product_delete, name='delete_product'),

    path('user/list/', user_list, name='user_list'),
    path('user/create/', user_add, name='create_user'),
    path('user/<int:pk>/edit', user_edit, name='edit_user'),
    path('user/<int:pk>/delete/', user_delete, name='delete_user'),

    path('order/list/', order_list, name='order_list'),
    path('customer_order/<int:id>/list/', customer_order_list, name='customer_order_list'),
    path('orderproduct/<int:id>/list', orderproduct_list, name='orderproduct_list'),
]