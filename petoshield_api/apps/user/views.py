from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as RestValidationError
from apps.core.utils import EmailSender, JwtToken, Validate
from apps.policy.models import Policy
from apps.user.filters import RoleFilter, UserFilter
from apps.user.models import Role, MailVerificationTokens
from apps.user.permissions import UserPermission
from django.utils.translation import gettext_lazy as _
from apps.user.serializers import (
    BaseUserSerializer,
    ExtendUserSerializer,
    RoleSerializer,
    RegisterUserSerializer,
    ResetPasswordSerializer,
    ChangePasswordSerializer)


@extend_schema(tags=['User'])
class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for managing user accounts.

    Attributes:
        queryset (QuerySet): The queryset of user objects.
        parser_classes (tuple): The parser classes used for request parsing.
        permission_classes (tuple): The permission classes used for user authentication and authorization.
        search_fields (list): The fields used for searching users.
        ordering_fields (list): The fields used for ordering users.
        ordering (str): The default ordering for users.
        filterset_class (FilterSet): The filterset class used for filtering users.

    Methods:
        get_serializer_class: Returns the appropriate serializer class based on the user's role.
        create: Create a new user account.
        me: Retrieve the current user's account details.
        verify_email: Verifies the user's email address.
        reset_password: Sends a password reset email to the user.
        reset_password_confirm: Resets the user's password.
        change_password: Change the user's password.
        destroy: Delete a user account.
    """

    queryset = get_user_model().objects.all()
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (UserPermission,)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = UserFilter

    def get_serializer_class(self):
        """Returns the appropriate serializer class based on the user's role.
        Returns:
            Serializer: The serializer class.
        """

        if self.request.user.is_staff:
            return ExtendUserSerializer
        return BaseUserSerializer

    def create(self, request, *args, **kwargs):
        """Creates a new user account.
        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: The response object.
        Raises:
            RestValidationError: If there is an error in the request data.
        """

        password = request.data.get('password')
        Validate.password_validation(password)
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        EmailSender.send_welcome_email(user)
        EmailSender.send_confirmation_email(user, request.META.get('HTTP_REFERER'))
        return Response(JwtToken.get_jwt_token(user), status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retrieves the current user's account details.
        Args:
            request (HttpRequest): The request object.
        Returns:
            Response: The response object.
        """

        user_serializer = BaseUserSerializer(request.user)
        return Response(user_serializer.data, status=200)

    @action(detail=False, methods=['post'])
    def verify_email(self, request):
        """Verifies the user's email address.
        Args:
            request (HttpRequest): The request object.
        Returns:
            Response: The response object.
        Raises:
            RestValidationError: If the email verification token is invalid.
        """

        token = request.data.get('token')
        mail_verification_token_instance = MailVerificationTokens.objects.filter(confirmation_token=token).first()
        if not mail_verification_token_instance:
            raise RestValidationError(_('Email verification fail'))
        get_user_model().objects.filter(pk=mail_verification_token_instance.user.id).update(is_verified=True)
        return Response({'message': _('Email was verified')}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        """Sends a reset password email to the user.
        Args:
            request (HttpRequest): The request object.
        Returns:
            Response: The response object.
        Raises:
            RestValidationError: If the user is not found with the provided email.
        """

        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_instance = get_user_model().objects.filter(email=serializer.data.get('email')).first()
        if not user_instance:
            raise RestValidationError(_(f'User not found with email: {serializer.data.get("email")}'))
        EmailSender.send_password_reset_email(user_instance, serializer.data.get('redirect_link'))
        return Response({'message': "Email was send"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def reset_password_confirm(self, request):
        """Resets the user's password.
        Args:
            request (HttpRequest): The request object.
        Returns:
            Response: The response object.
        Raises:
            RestValidationError: If the password reset token is invalid or the user is not found.
        """

        token = request.data.get('token')
        mail_verification_token_instance = MailVerificationTokens.objects.filter(confirmation_token=token).first()
        if not mail_verification_token_instance:
            raise RestValidationError(_('Invalid token'))
        user_instance = get_user_model().objects.filter(pk=mail_verification_token_instance.user.id).first()
        if not user_instance:
            raise RestValidationError(_('User not found'))
        password = request.data.get('password')
        Validate.password_validation(password)
        user_instance.set_password(request.data.get('password'))
        user_instance.save()
        return Response({'message': _('Password has been reset successfully')}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        """Changes the user's password.
        Args:
            request (HttpRequest): The request object.
        Returns:
            Response: The response object.
        Raises:
            RestValidationError: If the old password is incorrect.
        """

        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        user = request.user
        if not user.check_password(old_password):
            raise RestValidationError(_('Old password is not correct'))
        password = request.data.get('new_password')
        Validate.password_validation(password)
        user.set_password(new_password)
        user.save()
        EmailSender.send_reset_password_warning_email(user)
        return Response({'message': 'Password has been changed successfully'})

    def destroy(self, request, *args, **kwargs):
        """Deletes a user account.
        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: The response object.
        Raises:
            RestValidationError: If the user has active insurance subscriptions.
        """

        instance = self.get_object()
        policies = Policy.objects.filter(pet__user=instance, status='valid')
        if policies:
            raise RestValidationError(_('You have active insurance subscription, cancel them first'))
        # TODO: send email that account will be deleted
        return super().destroy(request, *args, **kwargs)


@extend_schema(tags=['Role'])
class RoleViewSet(viewsets.ModelViewSet):
    """API endpoint for managing roles.
    Attributes:
        serializer_class (Serializer): The serializer class for roles.
        queryset (QuerySet): The queryset of role objects.
        permission_classes (tuple): The permission classes used for user authentication and authorization.
        search_field (list): The fields used for searching roles.
        ordering_fields (list): The fields used for ordering roles.
        ordering (str): The default ordering for roles.
        filterset_class (FilterSet): The filterset class used for filtering roles.
    """

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    search_field = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = RoleFilter
