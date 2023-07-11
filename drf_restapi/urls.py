from django.urls import path, include
from drf_restapi import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix = 'viewsets', viewset = views.cha_viewset)

urlpatterns = [
    path('fbv/lst/', views.cha_lst, name='fbv-lst'),
    path('fbv/detail/<int:pk>', views.cha_detail, name='fbv-detail'),

    path('cbv/lst/', views.cha_lst1.as_view(), name='cbv-lst'),
    path('cbv/lst/detail/<int:pk>', views.cha_detail1.as_view(), name='cbv-detail'),

    path('gcbv/lst/', views.cha_lst2.as_view(), name='gcbv-lst'),
    path('gcbv/lst/detail/<int:pk>', views.cha_detail2.as_view(), name='gcbv-detail'),

    #path('viewsets/', views.cha_viewset.as_view(
    #    {'get': 'list',
    #    'post': 'create',}
    #    ), name = 'viewset-lst'),
    #path('viewsets/<int:pk>', views.cha_viewset.as_view(
    #    {'get': 'retrieve',
    #    'put': 'update',
    #    'patch': 'partial_update',
    #    'delete': 'destroy',
    #    }), name = 'viewset-detail')

    path('', include(router.urls))
    ]
