from rest_framework import permissions


class IsAuthenticatedAuthorOrReadOnly(permissions.IsAuthenticated):
    """Доступ только авторизованным, менять и удалять может только автор."""

    def has_object_permission(self, request, view, obj):
        # Авторизацию проверяет родительский класс, здесь проверяю автора:
        # читать можно всем, остальные методы пропускаю только автору.
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
