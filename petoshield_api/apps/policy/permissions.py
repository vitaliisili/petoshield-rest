from rest_framework import permissions


class ProviderPermissions(permissions.BasePermission):
    ROLES = ['admin', 'provider']

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff and request.user.is_authenticated
        elif view.action == 'create':
            return True
        elif view.action == 'retrieve':
            return request.user.is_authenticated and request.user.role.name in self.ROLES
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_authenticated and (request.user.is_staff or request.user.role.name == 'provider')
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff or obj.user == request.user
        return False


class PolicyPermissions(permissions.BasePermission):
    ROLES = ['client', 'admin', 'provider']

    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return request.user.role.name in self.ROLES
        elif view.action == 'create':
            return False
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return request.user.role.name in self.ROLES
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False


class InsuranceCasePermissions(permissions.BasePermission):
    ROLES = ['client', 'admin', 'provider']

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.role.name in self.ROLES
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.role.name in ['admin', 'provider']
        else:
            return False


class IncomingInvoicePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.role.name in ['admin', 'provider']
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff or obj.insurance_case.service_provider.user == request.user
        else:
            return False
