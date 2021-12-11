from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search'),
    path('featured/', views.featured, name='featured')
]
