"""xpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userposts import views
from newPost import views as newpv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('timeline/', include('timeline.urls')),
    path('posts/', include('userposts.urls')),
    path('profile/', include('userprofile.urls')),
    path('logout/', include('logout.urls')),
    path('newpost/', include('newPost.urls')),
    path('global/', include('global.urls')),
    path('following/', include('following.urls')),
    path('stat/', include('xpstat.urls')),
    path('deletePost/<int:id>', views.deletePost, name="deletePost"),
    path('updatepost/<int:id>', newpv.updatePost, name='updatepost'),
    path('likepost/', views.likePost, name='postlike'),
    path('dislikepost/', views.disLikePost, name='postdislike')
]
