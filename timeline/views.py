from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts
from timeline.models import Follower
# Create your views here.


@login_required(login_url='../login')
def timeline(response):
    myFollowing = Follower.objects.filter(follower_id=response.user.id)
    ids = []
    for f in myFollowing:
        ids.append(f.following_id)
    allPosts = Posts.objects.filter(author_id__in=ids).order_by('-dateOfPost')
    posts = []
    for i in allPosts:
        likeState = False
        dislikeState = False
        reportState = False
        if i.like.filter(id=response.user.id).count() != 0:
            likeState = True

        if i.dislike.filter(id=response.user.id).count() != 0:
            dislikeState = True

        if i.report.filter(id=response.user.id).count() != 0:
            reportState = True

        posts.append({
            'post': i,
            'likeState': likeState,
            'dislikeState': dislikeState,
            'reportState': reportState
        })
    return render(response, 'timeline/timeline.html', {'posts': posts})
