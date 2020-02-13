from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts
from timeline.models import Follower
# Create your views here.


@login_required(login_url='../login')
def timeline(response):
    myFollowing = Follower.objects.filter(follower_id=response.user.id)
    print(myFollowing)
    ids = []
    for f in myFollowing:
        ids.append(f.following_id)
    allPosts = Posts.objects.filter(author_id__in=ids).order_by('-dateOfPost')
    return render(response, 'timeline/timeline.html', {'posts': allPosts})
