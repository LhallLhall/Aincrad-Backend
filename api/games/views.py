from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CustomUser
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
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer
from rest_framework import status, permissions

# Create your views here.
def curl_call(request):
    url = "https://dir84il2yk.execute-api.us-west-2.amazonaws.com/production/v4/games"
    payload = "fields rating, cover.url ,id, name, genres.name, platforms.name, franchises.name, platforms.platform_logo.url, release_dates.human, summary; limit 500; where platforms != null; where release_dates != null; where rating > 98;"
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

class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)

# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

#     def get_query(self):
#         queryset = self.queryset
#         query_set = queryset.filter(id = self.request.user.id)
#         return query_set