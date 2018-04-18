from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/mnist/', views.mnist, name='test'),
]