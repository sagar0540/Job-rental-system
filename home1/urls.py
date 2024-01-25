from django.contrib import admin
from django.urls import path
from home1 import views

urlpatterns = [
    
    path('', views.signinn, name='signinn'),
    path('home/', views.home, name='home'),
    path('loginn/', views.loginn, name='loginn'),
    path('logoutt/', views.logoutt, name='logoutt'),
    path('inside/',views.inside,name="inside"),
    path('inside1/',views.inside1,name="inside1"),
    path('apply/',views.apply,name="apply"),
]


    


    

    
    
