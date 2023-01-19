
from django.urls import path
from . import views

urlpatterns = [
    path('', views.locator, name='Homepage'),
    path('Flavoursome/', views.index, name='Homepage'),
    path('Flavoursome/feedback/', views.feedback, name='Feedback'),
    path('Flavoursome/register/', views.register, name='Register'),
    path('Flavoursome/login/', views.login, name='Login'),
    path('Flavoursome/cart/', views.cart, name='Login'),
    path('Flavoursome/orders/', views.orders, name='Login'),
    path('Flavoursome/checkout/', views.checkout, name='checkout'),
    path('Flavoursome/updater/', views.updater, name='checkout'),
    path('Flavoursome/handler/', views.handler, name='Handler'),
]