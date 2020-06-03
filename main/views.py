from django.shortcuts import render
from .models import TweetObject
import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

# initial coordinates 
def mapCoordinates(request):
    '''
    get coordinates from db
    get any other information from db
    json encode all the data
    '''
    data  = TweetObject.objects.all()
    alldata = []
    u = 1
    for i in data:
        lats = ["lat", "long","hashtag","count"]
        coords = [i.latitude,i.longitude, i.hashtag, u]
        u+=1
        zipped = zip(lats,coords)
        alldata.append(dict(zipped))
    print(alldata)
    return JsonResponse(json.loads(json.dumps(alldata)), safe=False)

# heatmap coordinates
def heatmap(request):
    '''
    get data to be used in the heat map from db
    json encode all the data
    '''
    data  = TweetObject.objects.all()
    alldata = []
    u = 1
    for i in data:
        lats = ["lat", "long","count"]
        coords = [i.latitude,i.longitude, u]
        u+=1
        zipped = zip(lats,coords)
        alldata.append(dict(zipped))
    return JsonResponse(json.loads(json.dumps(alldata)), safe=False) 
