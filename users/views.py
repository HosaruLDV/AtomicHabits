from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import OwnerProfile
from users.serializers import UserSerializer, AllUserSerializer


class UserModelViewSet(ModelViewSet):
    """Контроллер для работы с юзером"""
    queryset = User.objects.all()

    def get_serializer_class(self):
        """При создании, обновлении и просмотре своего профиля доступны дополнительные поля"""
        if self.action in ['create', 'update']:
            return UserSerializer
        elif self.action == 'retrieve':
            if self.request.user == self.get_object():
                return UserSerializer
        return AllUserSerializer

    def get_permissions(self):
        """Создавать юзера могут все пользователи, остальной интерфейс доступен после авторизации"""
        if self.action == 'create':
            return [AllowAny()]
        return [OwnerProfile()]


class ChatIDUser(APIView):
    """Получение chat_id для регистрации"""
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        return Response({"url": "web.telegram.org/k/#@my_id_bot"})
