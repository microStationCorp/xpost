from django.urls import path
from . import views

urlpatterns = [
    path('follow/', views.following),
    path('', views.followPage, name='follow'),
    path('post/<str:usr>', views.followingPost, name='followingPost')
]
