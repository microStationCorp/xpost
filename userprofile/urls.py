from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.userProfile, name='profile'),
    path('likedpost', views.likedPost, name='likedpost')
]
