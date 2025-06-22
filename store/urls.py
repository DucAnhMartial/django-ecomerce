from django.urls import path

from . import views

urlpatterns = [
    path('',views.store, name='store'),
    path('product/<slug:slug>/', views.product_info, name='product_info'),
    path('category/<slug:category_slug>/', views.list_category, name='list_category')
]
