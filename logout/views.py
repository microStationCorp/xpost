from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.


def myLogout(response):
    logout(response)
    messages.info(response, 'successfully logged out')
    return redirect('../')
