
from django.urls import path
from . import views
from django.http import HttpResponse
#Create your views here.


urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    
]
