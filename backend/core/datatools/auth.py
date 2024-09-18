from rest_framework.authtoken.models import Token

from core import models


class AuthorizeError(Exception):
    pass


def authorize_user(credentials: dict) -> models.User:
    """Аутентификация пользователя"""
    user = models.User.objects.filter(username=credentials['username']).first()
    if not user:
        raise AuthorizeError('Неверный логин или пароль')

    if not user.check_password(credentials['password']):
        raise AuthorizeError('Неверный логин или пароль')

    Token.objects.get_or_create(user=user)

    return user
