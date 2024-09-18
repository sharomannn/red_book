from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core import datatools
from core import models
from core import serializers
from core import permissions


class Auth(APIView):
    """Аутентификация пользователя."""

    authentication_classes = []
    permission_classes = []

    @extend_schema(request=serializers.AuthorizeRequest, responses=serializers.AuthorizeResponse)
    def post(self, request: Request) -> Response:
        serializer = serializers.AuthorizeRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = datatools.authorize_user(serializer.validated_data)
        except datatools.AuthorizeError as ex:
            response_data = {'is_valid': False, 'msg': str(ex)}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        user_data = serializers.User(instance=user).data
        response_data = {'is_valid': True, 'token': user.auth_token.key, 'user': user_data}
        return Response(response_data)


class User(ModelViewSet):
    """Пользователи."""
    serializer_class = serializers.User
    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAdminOrIsModerator]

    @action(detail=False, methods=['get'])
    def current_user(self, request: Request) -> Response:
        """Получение данных текущего пользователя."""
        user_data = self.serializer_class(instance=self.request.user).data
        return Response(user_data)


class RedBookEntry(ModelViewSet):
    queryset = models.RedBookEntry
    serializer_class = serializers.RedBookEntry
    permission_classes = [permissions.IsAdminOrReadOnly]


class Observation(ModelViewSet):
    queryset = models.Observation.objects.all()
    serializer_class = serializers.Observation
    permission_classes = [permissions.IsAdminOrWriteOnly]
