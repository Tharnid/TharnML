from django.urls import path

# from .views  

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id/>', views.detail, name='detail'),
] 