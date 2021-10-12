from django.contrib import admin  
from consommation_energie import views  
from django.conf.urls import url
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('conso/', views.consommation_chart, name='conso-chart'),
]
 
 
