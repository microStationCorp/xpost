from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='../login')
def myLogout(response):
    logout(response)
    messages.info(response, 'successfully logged out')
    return redirect('../')
