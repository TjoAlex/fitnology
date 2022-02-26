"""Url path for profile page"""
from django.urls import path
from . import views

# inspired by boutique ado mini project
# adapted for this project


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history')
]
