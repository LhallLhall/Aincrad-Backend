from django.urls import path, include
from .views import curl_call
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate, UserDetail, GameViewSet

router = routers.SimpleRouter()
router.register(r'game', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addGameToUser/<int:gameID>/', views.addGameToUser),
    path('api/', views.curl_call, name='game json'),
    path('search/<game>', views.search_curl_call, name='search'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('users/<int:pk>', UserDetail.as_view(), name="get_user_details"),
]