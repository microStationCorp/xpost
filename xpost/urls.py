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
    path('dislikepost/', views.disLikePost, name='postdislike'),
    path('reportpost/', views.reportPost, name='postreport')
]
