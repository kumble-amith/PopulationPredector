from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home , name = 'home'),
    path('predectionResult', views.predectionResult ,name = 'predectionResult')
]