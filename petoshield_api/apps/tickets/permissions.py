from rest_framework import permissions

class AnyCreateOnlyStaffUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        else:
            return request.user.is_authenticated and request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        if view.action == 'create':
            return True
        else:
            return request.user.is_authenticated and request.user.is_staff
