from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.forms.models import model_to_dict
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import requests
import json
from django.views import View
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer
from rest_framework import status, permissions

# Create your views here.
def curl_call(request):
    url = "https://dir84il2yk.execute-api.us-west-2.amazonaws.com/production/v4/games"
    payload = "fields rating, cover.url ,id, name, genres.name, platforms.name, franchises.name, platforms.platform_logo.url, release_dates.human, summary, involved_companies.company.name, storyline; limit 500; where platforms != null; sort rating desc;"
    #  where rating != null; where genres != null; where release_dates != null; where platforms != null; where summary != null;
    headers = {
    'x-api-key': 'HEQsMFqOnt1zD2q1oLwo36jxVFeiavom57v2F0Ud',
    'Client-ID': 'e4e2unaghoyw3t7zz80w1gteqidkaz',
    'Authorization': 'Bearer ea7k5q6odr0g2osf71krx9dxxa1koi',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    return JsonResponse(response, safe=False)

def search_curl_call(request, game):
    url = "https://dir84il2yk.execute-api.us-west-2.amazonaws.com/production/v4/games/"
    payload = f'search "{game}"; fields rating, cover.url ,id, name, genres.name, platforms.name, franchises.name, platforms.platform_logo.url, release_dates.human, summary, involved_companies.company.name, storyline; limit 21; where platforms != null; where genres != null; where release_dates != null;'
    #  where rating != null; where genres != null; where release_dates != null; where platforms != null; where summary != null;
    headers = {
    'x-api-key': 'HEQsMFqOnt1zD2q1oLwo36jxVFeiavom57v2F0Ud',
    'Client-ID': 'e4e2unaghoyw3t7zz80w1gteqidkaz',
    'Authorization': 'Bearer ea7k5q6odr0g2osf71krx9dxxa1koi',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    return JsonResponse(response, safe=False)

class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# class HelloWorldView(APIView):

#     def get(self, request):
#         return Response(data={"hello":"world"}, status=status.HTTP_200_OK)

class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        obj = self.queryset.get(game_id=self.request.data["game_id"])
        return obj

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        kwargs['partial'] = True
        try:
            game = Game.objects.get(game_id=request.data["game_id"])
            return super().retrieve(request)
        except Game.DoesNotExist:
            return super().create(request, *args, **kwargs)

class GameUserViewSet(ModelViewSet):
    queryset = GameUser.objects.all()
    serializer_class = GameUserSerializer

@api_view([ 'POST', 'DELETE'])
def addGameToUser(request, gameID):
    print(request)
    user = CustomUser.objects.get(id = request.user.id)
    game = Game.objects.get(game_id = gameID)

    if request.method == "POST":
        user.games.add(game)
    
    if request.method == 'DELETE':
        user.games.remove(game)

    gameSerializer = GameSerializer(game)
    return Response(gameSerializer.data)

# @api_view(['GET'])
# def getUserGames(request, userId):
#     # user = CustomUser.objects.get(id = userId)
#     # games = Game.objects.filter(  = userId)
#     serializer = GameSerializer(game)
#     return Response(serializer.data)