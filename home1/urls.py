from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('loginn',views.loginn,name='loginn'),

    path('signinn',views.signinn,name='signinn')
    

    
    
]