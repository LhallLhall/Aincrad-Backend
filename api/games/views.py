from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import Song
from django.forms.models import model_to_dict
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import generics
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import requests
import json
from django.views import View

# Create your views here.
def curl_call(request):
    url = "https://dir84il2yk.execute-api.us-west-2.amazonaws.com/production/v4/games"
    payload = "fields id, name, genres.name, platforms.name, franchises.name, screenshots.url, aggregated_rating, release_dates.human, summary, videos.video_id; limit 500;"
    headers = {
    'x-api-key': 'HEQsMFqOnt1zD2q1oLwo36jxVFeiavom57v2F0Ud',
    'Client-ID': 'e4e2unaghoyw3t7zz80w1gteqidkaz',
    'Authorization': 'Bearer ea7k5q6odr0g2osf71krx9dxxa1koi',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    return JsonResponse(response, safe=False)