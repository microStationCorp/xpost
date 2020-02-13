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
        for f in myFollow:
            if f.following_id == post.author_id:
                posts.append({
                    'post': post,
                    'indication': 'follow',
                    'color': 'text-primary'
                })
                flag = True
                break
        if post.author_id == response.user.id:
            posts.append({
                'post': post,
                'indication': '',
                'color': 'text-success'
            })
        elif flag == False:
            posts.append({
                'post': post,
                'indication': 'unfollow',
                'color': 'text-success'
            })
        else:
            flag = False
    return render(response, 'global/global.html', {'posts': posts})
