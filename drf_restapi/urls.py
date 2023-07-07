from django.urls import path, include
from drf_restapi import views

urlpatterns = [
    path('fbv/lst/', views.cha_lst, name='fbv-lst'),
    path('fbv/detail/<int:pk>', views.cha_detail, name='fbv-detail'),
    ]
