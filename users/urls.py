from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserModelViewSet, ChatIDUser

app_name = UsersConfig.name
router = DefaultRouter()
router.register(r'', UserModelViewSet, basename='user')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chat_id/', ChatIDUser.as_view(), name='chat_id'),
    ] + router.urls