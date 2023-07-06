from django.urls import path, include
from drf_restapi import views

urlpatterns = [
    path('fbv/lst/', views.cha_lst, name='fbv-lst')
    ]
