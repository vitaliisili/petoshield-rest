from rest_framework import permissions

class IsStaffOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        else:
            return request.user.is_authenticated and request.user.is_staff
            

    def has_object_permission(self, request, view, obj):
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return (obj.user == request.user.username and request.user.is_authenticated) or request.user.is_staff
        return True