from rest_framework import permissions

class AnyCreateOnlyStaffUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' or request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        
        return request.user.is_authenticated and request.user.is_staff 