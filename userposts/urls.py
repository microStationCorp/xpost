from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.userPost, name='userPost'),
    path('countPost/', views.myPostCount, name='postCount'),
]
