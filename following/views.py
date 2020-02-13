from django.shortcuts import render, HttpResponse
from timeline.models import Follower
from django.http import JsonResponse

# Create your views here.


def following(response):
    if response.method == "GET" and response.is_ajax():
        followingId = response.GET['id']
        indicator = response.GET['indicator']
        if indicator == 'follow':
            Follower.objects.create(
                follower_id=response.user.id, following_id=followingId)
            context = {
                'rmc': 'text-primary',
                'ac': 'text-success',
                'text': 'unfollow'
            }
        elif indicator == 'unfollow':
            Follower.objects.filter(
                follower_id=response.user.id, following_id=followingId)[0].delete()
            context = {
                'rmc': 'text-success',
                'ac': 'text-primary',
                'text': 'follow'
            }
        # if response.GET['indicator'] == 'follow':
        #     Follower.objects.Create(
        #         follower_id=response.user.id, following_id=followingId)
        # elif response.GET['indicator'] == 'unfollow':
        #     Follower.objects.filter(follower_id=response.user.id,
        #                             following_id=followingId)[0].delete()
        return JsonResponse(context)
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
