from django.urls import path, include
from .views import curl_call
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate, UserDetail, GameViewSet

router = routers.SimpleRouter()
router.register(r'game', GameViewSet)
# router.register(r'gameUser', GameUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('addGameToUser/<int:gameID>/', views.addGameToUser), #makes the connection to the user and a game either saved in the database or created
    path('getUserGames', views.getUserGames), #grabs all games to the user
    path('api/', views.curl_call, name='game json'),
    path('updateCompletion/<int:gameID>', views.updateCompletion),
    path('updateGameHours/<int:gameID>', views.updateGameHours),
    path('updateGameTimer/<int:gameID>', views.updateGameTimer),
    path('search/<game>', views.search_curl_call, name='search'), #return all items that are related to the inputed game
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>', UserDetail.as_view(), name="get_user_details"),
]