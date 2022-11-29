from django.urls import path, include
from .views import curl_call
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/', views.curl_call, name='game json')
]