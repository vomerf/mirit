from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/perfomer_list/', views.perfomer_list_order, name='perfomer_list'),
    path('profile/<str:username>/customer_list/', views.perfomer_list_order, name='customer_list'),
    path('order_list/', views.list_orders, name='order_list'),
    path('accept_order/<int:pk>/', views.accept_order, name='accept_order'),
    path('canceled_order/<int:pk>/', views.canceled_order, name='canceled_order'),
]