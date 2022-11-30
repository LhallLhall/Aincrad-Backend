from django.urls import path, include
from .views import curl_call
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate, HelloWorldView
router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/', views.curl_call, name='game json'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    # path('user/', UserViewSet.as_view())
]