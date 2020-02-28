from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userposts.models import Posts

# Create your views here.


@login_required(login_url='../login')
def userProfile(response):
    return render(response, 'userprofile/profile.html')

@login_required(login_url='../login')
def likedPost(response):
    pass
