from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.start, name='Team No.'),
    path('p1', views.comp1, name='room304'),
    # path('p2', views.p2, name='GWOI'),
    # path('p3', views.p3, name='BM'),
    # path('p4', views.p4, name='Regal'),
    # path('p5', views.p5, name='CSB'),
    # path('qr/', views.qr, name='QR read'),
]