from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_move/', views.process_move, name='process_move'),
    
]


