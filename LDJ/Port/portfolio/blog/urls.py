from django.urls import path

# from .views  

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
] 