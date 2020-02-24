from django.shortcuts import render, HttpResponse
from timeline.models import Follower
from userposts.models import Posts
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='../login')
def followPage(response):

    myFollow = Follower.objects.filter(follower_id=response.user.id)
    myFollowingUser = []

    for f in myFollow:
        myFollowingUser.append({
            'usr': User.objects.filter(id=f.following_id)
        })
    posts = Posts.objects.filter(
        author_id=myFollowingUser[0]['usr'][0].id).order_by('-dateOfPost')
    context = {
        'myFollow': myFollowingUser,
        'posts': posts
    }
    return render(response, 'following/follow.html', context)


@login_required(login_url='../login')
def followingPost(response, usr):
    if response.method == "GET" and response.is_ajax():
        user = User.objects.filter(username=usr)[0]
        posts = Posts.objects.filter(author_id=user.id).order_by('-dateOfPost')
        allposts = []
        for post in posts:
            allposts.append({
                'title': post.title,
                'time': post.dateOfPost,
                'post': post.post,
                'like':post.like.count(),
                'dislike':post.dislike.count(),
                'report':post.report.count(),
            })
        data = {
            'allposts': allposts
        }
        return JsonResponse(data)
    else:
        return HttpResponse('''<h1 style="border-bottom: 1px solid #aaa; padding: 10px" > Not Found(  # 404)</h1>

    <div class="alert alert-danger" >
        Page not found. </div >

    <p>
        The above error occurred while the Web server was processing your request.
    </p>
    <p>
        Please contact us if you think this is a server error. Thank you.
    </p>''')


@login_required(login_url='../login')
def followCount(response):
    if response.method == "GET" and response.is_ajax():
        return HttpResponse(Follower.objects.filter(follower_id=response.user.id).count())
    else:
        return HttpResponse('''<h1 style="border-bottom: 1px solid #aaa; padding: 10px" > Not Found(  # 404)</h1>

    <div class="alert alert-danger" >
        Page not found. </div >

    <p>
        The above error occurred while the Web server was processing your request.
    </p>
    <p>
        Please contact us if you think this is a server error. Thank you.
    </p>''')


@login_required(login_url='../login')
def following(response):
    if response.method == "GET" and response.is_ajax():
        followingId = response.GET['id']
        indicator = response.GET['indicator']
        if indicator == 'follow':
            Follower.objects.create(
                follower_id=response.user.id, following_id=followingId)
            context = {
                'rmc': 'text-primary',
                'ac': 'text-success',
                'text': 'unfollow'
            }
        elif indicator == 'unfollow':
            Follower.objects.filter(
                follower_id=response.user.id, following_id=followingId)[0].delete()
            context = {
                'rmc': 'text-success',
                'ac': 'text-primary',
                'text': 'follow'
            }
        return JsonResponse(context)
    else:
        return HttpResponse('''<h1 style="border-bottom: 1px solid #aaa; padding: 10px" > Not Found(  # 404)</h1>

    <div class="alert alert-danger" >
        Page not found. </div >

    <p>
        The above error occurred while the Web server was processing your request.
    </p>
    <p>
        Please contact us if you think this is a server error. Thank you.
    </p>''')
