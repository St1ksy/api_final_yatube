from rest_framework import permissions


# Класс для пользовательского разрешения, которое ограничивает доступ
# к объектам, основываясь на том, является ли пользователь автором объекта
# или запрос использует безопасный метод.
class IsAuthorOrReadOnly(permissions.BasePermission):
    # Метод проверяет, есть ли у пользователя разрешение на выполнение запроса.
    # Разрешение предоставляется, если метод запроса безопасный (GET, OPTIONS, HEAD).
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    # Метод проверяет разрешение на доступ к конкретному объекту.
    # Разрешение предоставляется, если метод запроса безопасный,
    # или если текущий пользователь является автором объекта.
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
