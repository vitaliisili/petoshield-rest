from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ['create', 'reset_password', 'reset_password_confirm']:
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy', 'me']:
            return request.user.is_authenticated
        elif view.action == 'verify_email':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        elif view.action == 'me':
            return obj == request.user
        elif view.action in ['verify_email', 'reset_password', 'reset_password_confirm']:
            return True
        else:
            return False
