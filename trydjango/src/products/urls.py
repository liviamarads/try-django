from django.urls import path
from .views import (product_detail_view,
                            product_create_view,
                            render_initial_data,
                            product_update_view,
                            product_delete_view,
                            product_list_view
                            )

# from django.contrib import admin
# from django.urls import include, path
#
# from pages.views import home_view, contac_view, about_view

app_name = 'products'
urlpatterns = [

    path('<int:id>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'),
]
