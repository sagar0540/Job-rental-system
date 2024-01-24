from django.contrib import admin
from django.urls import path
from home1 import views

urlpatterns = [
    
    path('', views.signinn, name='signinn'),
    path('home/', views.home, name='home'),
    path('loginn/', views.loginn, name='loginn'),
]


    


    

    
    
