from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Posts
# Create your views here.


@login_required(login_url='../login')
def userPost(response):
    myPost = Posts.objects.filter(
        author_id=response.user.id).order_by('-dateOfPost')
    posts = []
    for i in myPost:
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
    return render(response, 'userposts/userposts.html', {'posts': posts})


@login_required(login_url='../login')
def myPostCount(response):
    if response.method == "GET" and response.is_ajax():
        return HttpResponse(Posts.objects.filter(author_id=response.user.id).count())
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
def deletePost(response, id):
    if len(Posts.objects.filter(id=id, author_id=response.user.id)) != 0:
        Posts.objects.filter(id=id)[0].delete()
        return redirect('../posts')
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
def likePost(response):
    if response.method == "GET" and response.is_ajax():
        # when not disliked and want to like
        if Posts.objects.filter(id=response.GET['postid'], like__id=response.user.id).count() == 0 and Posts.objects.filter(id=response.GET['postid'], dislike__id=response.user.id).count() == 0:
            Posts.objects.get(
                id=response.GET['postid']).like.add(response.user)
            data = {
                'like-count': Posts.objects.get(id=response.GET['postid']).like.count(),
                'like-action': 'increase',
            }
        # when disliked and want to like
        elif Posts.objects.filter(id=response.GET['postid'], like__id=response.user.id).count() == 0 and Posts.objects.filter(id=response.GET['postid'], dislike__id=response.user.id).count() != 0:
            Posts.objects.get(
                id=response.GET['postid']).dislike.remove(response.user)
            Posts.objects.get(
                id=response.GET['postid']).like.add(response.user)
            data = {
                'like-count': Posts.objects.get(id=response.GET['postid']).like.count(),
                'dislike-count': Posts.objects.get(id=response.GET['postid']).dislike.count(),
                'like-action': 'increase-disliked',
            }
        # when already liked
        else:
            Posts.objects.get(
                id=response.GET['postid']).like.remove(response.user)
            data = {
                'like-count': Posts.objects.get(id=response.GET['postid']).like.count(),
                'like-action': 'decrease',
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
def disLikePost(response):
    if response.method == "GET" and response.is_ajax():
        # when not liked and want to dislike
        if Posts.objects.filter(id=response.GET['postid'], dislike__id=response.user.id).count() == 0 and Posts.objects.filter(id=response.GET['postid'], like__id=response.user.id).count() == 0:
            Posts.objects.get(
                id=response.GET['postid']).dislike.add(response.user)
            data = {
                'dislike-count': Posts.objects.get(id=response.GET['postid']).dislike.count(),
                'dislike-action': 'increase',
            }
        # when liked and want to dislike
        elif Posts.objects.filter(id=response.GET['postid'], like__id=response.user.id).count() != 0 and Posts.objects.filter(id=response.GET['postid'], dislike__id=response.user.id).count() == 0:
            Posts.objects.get(
                id=response.GET['postid']).dislike.add(response.user)
            Posts.objects.get(
                id=response.GET['postid']).like.remove(response.user)
            data = {
                'dislike-count': Posts.objects.get(id=response.GET['postid']).dislike.count(),
                'like-count': Posts.objects.get(id=response.GET['postid']).like.count(),
                'dislike-action': 'increase-liked',
            }
            pass
        # when already liked
        else:
            Posts.objects.get(
                id=response.GET['postid']).dislike.remove(response.user)
            data = {
                'dislike-count': Posts.objects.get(id=response.GET['postid']).dislike.count(),
                'dislike-action': 'decrease',
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
def reportPost(response):
    if response.method == "GET" and response.is_ajax():
        if Posts.objects.filter(id=response.GET['postid'], report__id=response.user.id).count() == 0:
            Posts.objects.get(
                id=response.GET['postid']).report.add(response.user)
            data = {
                'report-count': Posts.objects.get(id=response.GET['postid']).report.count(),
                'report-action': 'increase',
            }
        else:
            Posts.objects.get(
                id=response.GET['postid']).report.remove(response.user)
            data = {
                'report-count': Posts.objects.get(id=response.GET['postid']).report.count(),
                'report-action': 'decrease',
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
