from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_product, name='add-product'),
    path('substract/<int:product_id>/', views.substract_product, name='substract-product'),
    path('remove/<int:product_id>/', views.remove_product, name='remove-product'),
    path('clear/', views.clear_cart, name='clear-cart'),
]
