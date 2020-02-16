from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Posts
# Create your views here.


@login_required(login_url='../login')
def userPost(response):
    myPost = Posts.objects.filter(
        author_id=response.user.id).order_by('-dateOfPost')
    return render(response, 'userposts/userposts.html', {'posts': myPost})


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
