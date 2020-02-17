from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import newPostForm
from userposts.models import Posts
# Create your views here.


@login_required(login_url='../login')
def newpost(response):
    if response.method == 'POST':
        form = newPostForm(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            myPost = Posts(title=title, post=post, author_id=response.user.id)
            myPost.save()
            return redirect('../posts')
    else:
        form = newPostForm()
    return render(response, 'newPost/newpost.html', {'form': form})


@login_required(login_url='../login')
def updatePost(response, id):
    if response.method == 'POST':
        form = newPostForm(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            Posts.objects.filter(id=id, author_id=response.user.id).update(title=title, post=post)
            return redirect('../posts')
    else:
        post = Posts.objects.filter(id=id, author_id=response.user.id)[0]
        form = newPostForm(initial={'title': post.title, 'post': post.post})
    return render(response, 'newPost/update.html', {'form': form,'id':id})
