from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts
from timeline.models import Follower
# Create your views here.


@login_required(login_url='../login')
def globalPost(response):
    allPosts = Posts.objects.all().order_by('-dateOfPost')
    myFollow = Follower.objects.filter(follower_id=response.user.id)
    return render(response, 'global/global.html', {'posts': allPosts, 'myFollow': myFollow})
