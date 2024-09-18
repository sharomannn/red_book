from rest_framework import permissions


class IsAdminOrWriteOnly(permissions.BasePermission):
    """
    Разрешает редактировать объект только администраторам. Остальные пользователи могут только создавать записи.
    """

    def has_permission(self, request, view):
        # Разрешить создание (POST) всем пользователям
        if request.method == 'POST':
            return True

        # Для остальных методов требуется быть администратором
        return request.user and (
            request.user.is_staff or request.user.is_superuser or getattr(request.user, 'is_moderator', False)
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешает только администраторам изменять данные.
    Чтение доступно для всех пользователей.
    """

    def has_permission(self, request, view):
        # Разрешаем чтение (GET) для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Для остальных методов требуется быть администратором
        return request.user and (request.user.is_staff or request.user.is_superuser or request.user.is_moderator)


class IsAdminOrIsModerator(permissions.BasePermission):
    """
    Разрешает редактировать объект только администраторам или модераторам.
    """

    def has_permission(self, request, view):
        # Разрешаем чтение (GET) для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Для остальных методов требуется быть администратором
        return request.user and (request.user.is_staff or request.user.is_superuser or request.user.is_moderator)
