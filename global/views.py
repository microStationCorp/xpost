from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts
# Create your views here.


@login_required(login_url='../login')
def globalPost(response):
    allPosts = Posts.objects.all().order_by('-dateOfPost')
    return render(response, 'global/global.html', {'posts': allPosts})
