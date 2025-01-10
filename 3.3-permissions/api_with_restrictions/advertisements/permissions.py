from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Дает доступ для изменения или удаления только автору объявления.
    """
    def has_object_permission(self, request, view, obj):
        # Для безопасных методов (GET, HEAD, OPTIONS) доступ разрешён
        if request.method in SAFE_METHODS:
            return True
        # Для изменений и удаления разрешение даётся только автору объявления
        return obj.creator == request.user
