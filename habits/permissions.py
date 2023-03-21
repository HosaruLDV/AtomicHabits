from rest_framework.permissions import BasePermission


class OwnerHabit(BasePermission):
    """CRUD доступ к своим привычкам"""
    def has_permission(self, request, view):
        if view.action in ['update', 'destroy', 'retrieve']:
            return request.user == view.get_object().user
        return request.user.is_authenticated