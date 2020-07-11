from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello world</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    Rest API View 
    Consume by JavaScript or Swift/Java/iOS/Android
    return JSON data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status) # Json.dumps content_type='application/json'
