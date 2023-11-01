from rest_framework import permissions


class BreedPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'list':
            return True
        elif view.action == 'retrieve':
            return request.user.is_authenticated and request.user.role.name in ['client', 'admin']
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        return False


class PetPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated and request.user.role.name in ['client', 'admin']
        elif view.action == 'create_new_account':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj.user == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update', 'destroy']:
            return obj.user == request.user or request.user.is_staff
        else:
            return False
