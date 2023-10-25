from rest_framework import permissions

class IsStaffOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create':
            if view.basename == 'breeds':
                return request.user.is_authenticated and request.user.is_staff
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            if view.basename == 'breeds':
                return True
            return obj.user == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update', 'destroy']:
            if view.basename == 'breeds':
                return request.user.is_staff
            return obj.user == request.user or request.user.is_staff
        else:
            return False