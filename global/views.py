from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts
from timeline.models import Follower
# Create your views here.


@login_required(login_url='../login')
def globalPost(response):
    flag = False
    posts = []
    allPosts = Posts.objects.all().order_by('-dateOfPost')
    myFollow = Follower.objects.filter(follower_id=response.user.id)
    for post in allPosts:
        likeState = False
        dislikeState = False
        reportState = False
        if post.like.filter(id=response.user.id).count() != 0:
            likeState = True

        if post.dislike.filter(id=response.user.id).count() != 0:
            dislikeState = True

        if post.report.filter(id=response.user.id).count() != 0:
            reportState = True

        for f in myFollow:
            if f.following_id == post.author_id:
                posts.append({
                    'post': post,
                    'indication': 'unfollow',
                    'color': 'text-success',
                    'likeState': likeState,
                    'dislikeState': dislikeState,
                    'reportState': reportState
                })
                flag = True
                break
        if post.author_id == response.user.id:
            posts.append({
                'post': post,
                'indication': '',
                'color': 'text-success',
                'likeState': likeState,
                'dislikeState': dislikeState,
                'reportState': reportState
            })
        elif flag == False:
            posts.append({
                'post': post,
                'indication': 'follow',
                'color': 'text-primary',
                'likeState': likeState,
                'dislikeState': dislikeState,
                'reportState': reportState,
            })
        else:
            flag = False
    return render(response, 'global/global.html', {'posts': posts})
