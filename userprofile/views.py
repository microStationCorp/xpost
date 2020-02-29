from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts
from timeline.models import Follower
from django.http import JsonResponse, HttpResponse

# Create your views here.


@login_required(login_url='../login')
def userProfile(response):
    allposts = Posts.objects.filter(author__id=response.user.id)[:5]
    posts = []
    sl = 0
    for p in allposts:
        sl += 1
        posts.append({
            'sl': sl,
            'post': p,
            'count': p.like.count()
        })
    posts.sort(key=compare, reverse=True)

    myFollowing = Follower.objects.filter(follower_id=response.user.id).count()
    myFollower = Follower.objects.filter(following_id=response.user.id).count()
    context = {
        'posts': posts[:5],
        'username': response.user,
        'email': response.user.email,
        'following': myFollowing,
        'follower': myFollower
    }
    return render(response, 'userprofile/profile.html', context)


def compare(obj):
    return obj['count']


@login_required(login_url='../login')
def poststatus(response):
    if response.method == "GET" and response.is_ajax():
        allposts = Posts.objects.filter(author__id=response.user.id)
        posts = []
        sl = 0
        count = 0

        for p in allposts:
            sl += 1
            if response.GET['dashId'] == 'likes':
                count = p.like.count()
                posts.append({
                    'sl': sl,
                    'title': p.title,
                    'dop': p.dateOfPost,
                    'count': count,
                    'type': response.GET['dashId']
                })
            elif response.GET['dashId'] == 'dislikes':
                count = p.dislike.count()
                posts.append({
                    'sl': sl,
                    'title': p.title,
                    'dop': p.dateOfPost,
                    'count': count,
                    'type': response.GET['dashId']
                })
            else:
                count = p.report.count()
                posts.append({
                    'sl': sl,
                    'title': p.title,
                    'dop': p.dateOfPost,
                    'count': count,
                    'type': response.GET['dashId']
                })

        posts.sort(key=compare, reverse=True)

        data = {
            'posts': posts[:5]
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
