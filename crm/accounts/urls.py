from django.urls import path

#import views first to connect with urls
from . import views

urlpatterns = [
    path('', views.Home),
]