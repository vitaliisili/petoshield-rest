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
    """API endpoint for managing user accounts."""

    queryset = get_user_model().objects.all()
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = (UserPermission,)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = UserFilter

    def get_serializer_class(self):
        """Returns the appropriate serializer class based on the user's role."""

        if self.request.user.is_staff:
            return ExtendUserSerializer
        return BaseUserSerializer

    def create(self, request, *args, **kwargs):
        """Creates a new user account."""

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
        """Retrieves the current user's account details."""

        user_serializer = BaseUserSerializer(request.user)
        return Response(user_serializer.data, status=200)

    @action(detail=False, methods=['post'])
    def verify_email(self, request):
        """Verifies the user's email address."""

        token = request.data.get('token')
        mail_verification_token_instance = MailVerificationTokens.objects.filter(confirmation_token=token).first()

        if not mail_verification_token_instance:
            raise RestValidationError(_('Email verification fail'))

        get_user_model().objects.filter(pk=mail_verification_token_instance.user.id).update(is_verified=True)
        return Response({'message': _('Email was verified')}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        """Sends a reset password email to the user."""

        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_instance = get_user_model().objects.filter(email=serializer.data.get('email')).first()
        if not user_instance:
            raise RestValidationError(_(f'User not found with email: {serializer.data.get("email")}'))

        EmailSender.send_password_reset_email(user_instance, serializer.data.get('redirect_link'))
        return Response({'message': "Email was send"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def reset_password_confirm(self, request):
        """Resets the user's password."""

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
        """Changes the user's password."""

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
        """Deletes a user account."""

        instance = self.get_object()
        policies = Policy.objects.filter(pet__user=instance, status='valid')

        if policies:
            raise RestValidationError(_('You have active insurance subscription, cancel them first'))

        email_data = {
            "name": instance.name,
            "email": instance.email,
        }

        EmailSender.send_mail_account_deleted(email_data)

        return super().destroy(request, *args, **kwargs)


@extend_schema(tags=['Role'])
class RoleViewSet(viewsets.ModelViewSet):
    """API endpoint for managing roles."""

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    search_field = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = RoleFilter
