from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.userProfile, name='profile'),
    path('poststatus/', views.poststatus, name='likedpost')
]
