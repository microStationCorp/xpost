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
def deletePost(response, id):
    Posts.objects.filter(id=id)[0].delete()
    return redirect('../posts')
