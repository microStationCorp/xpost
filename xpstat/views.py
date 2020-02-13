from django.shortcuts import render

# Create your views here.


def xstat(response):
    return render(response, 'xpstat/stat.html')
