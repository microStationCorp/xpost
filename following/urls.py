from django.urls import path
from . import views

urlpatterns = [
    path('follow/', views.following),
    path('', views.followPage, name='follow')
]
