from rest_framework import permissions


class ProviderPermissions(permissions.BasePermission):
    """Custom permission class for provider-related actions.
    Attributes:
        ROLES (list): The list of roles allowed for certain actions.
    Methods:
        has_permission: Checks if the user has permission for the requested action.
        has_object_permission: Checks if the user has permission for the requested object action.
    """

    ROLES = ['admin', 'provider']

    def has_permission(self, request, view):
        """Checks if the user has permission for the requested action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

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
        """Checks if the user has permission for the requested object action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
            obj: The object related to the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

        if not request.user.is_authenticated:
            return False
        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff or obj.user == request.user
        return False


class PolicyPermissions(permissions.BasePermission):
    """Custom permission class for policy-related actions.
    Attributes:
        ROLES (list): The list of roles allowed for certain actions.
    Methods:
        has_permission: Checks if the user has permission for the requested action.
        has_object_permission: Checks if the user has permission for the requested object action.
    """

    ROLES = ['client', 'admin', 'provider']

    def has_permission(self, request, view):
        """Checks if the user has permission for the requested action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

        if view.action in ['retrieve', 'list']:
            return request.user.role.name in self.ROLES
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """Checks if the user has permission for the requested object action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
            obj: The object related to the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

        if view.action == 'retrieve':
            return request.user.role.name in self.ROLES
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False


class InsuranceCasePermissions(permissions.BasePermission):
    """Custom permission class for insurance-case related actions.
    Attributes:
        ROLES (list): The list of roles allowed for certain actions.
    Methods:
        has_permission: Checks if the user has permission for the requested action.
        has_object_permission: Checks if the user has permission for the requested object action.
    """

    ROLES = ['client', 'admin', 'provider']

    def has_permission(self, request, view):
        """Checks if the user has permission for the requested action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

        if view.action in ['list', 'retrieve']:
            return request.user.role.name in self.ROLES
        elif view.action in ['create']:
            return request.user.role.name in ['admin', 'provider']
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.role.name in ['admin']
        else:
            return False


class IncomingInvoicePermissions(permissions.BasePermission):
    """Custom permission class for incoming invoice-related actions.
    Methods:
        has_permission: Checks if the user has permission for the requested action.
        has_object_permission: Checks if the user has permission for the requested object action.
    """

    def has_permission(self, request, view):
        """Checks if the user has permission for the requested action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

        if view.action in ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.role.name in ['admin', 'provider']
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """Checks if the user has permission for the requested object action.
        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object associated with the action.
            obj: The object related to the action.
        Returns:
            bool: True if the user has permission, False otherwise.
        """

        if view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff or obj.insurance_case.service_provider.user == request.user
        else:
            return False
