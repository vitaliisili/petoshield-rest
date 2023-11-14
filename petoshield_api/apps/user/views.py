from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from apps.core.utils import EmailSender, JwtToken
from apps.user.filters import RoleFilter, UserFilter
from apps.user.models import Role, MailVerificationTokens
from apps.user.permissions import UserPermission
from django.utils.translation import gettext_lazy as _
from apps.user.serializers import BaseUserSerializer, ExtendUserSerializer, RoleSerializer, RegisterUserSerializer, \
    ResetPasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (UserPermission,)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ExtendUserSerializer
        return BaseUserSerializer

    def create(self, request, *args, **kwargs):
        try:
            validate_password(request.data.get('password'))
        except ValidationError as error:
            raise RestValidationError(error)

        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        EmailSender.send_confirmation_email(user, request.META.get('HTTP_REFERER'))  # TODO: Send welcome message

        return Response(JwtToken.get_jwt_token(user), status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def me(self, request):
        user_serializer = BaseUserSerializer(request.user)
        return Response(user_serializer.data, status=200)

    @action(detail=False, methods=['post'])
    def verify_email(self, request):
        token = request.data.get('token')
        mail_verification_token_instance = MailVerificationTokens.objects.filter(confirmation_token=token).first()

        if not mail_verification_token_instance:
            raise RestValidationError(_('Email verification fail'))

        get_user_model().objects.filter(pk=mail_verification_token_instance.user.id).update(is_verified=True)

        return Response({'message': _('Email was verified')}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def reset_password(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_instance = get_user_model().objects.filter(email=serializer.data.get('email')).first()

        if not user_instance:
            raise RestValidationError(_(f'User not found with email: {serializer.data.get("email")}'))

        EmailSender.send_password_reset_email(user_instance, serializer.data.get('redirect_link'))
        return Response({'message': "Email was send"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def reset_password_confirm(self, request):
        token = request.data.get('token')
        mail_verification_token_instance = MailVerificationTokens.objects.filter(confirmation_token=token).first()

        if not mail_verification_token_instance:
            raise RestValidationError(_('Invalid token'))

        user_instance = get_user_model().objects.filter(pk=mail_verification_token_instance.user.id).first()

        if not user_instance:
            raise RestValidationError(_('User not found'))

        try:
            validate_password(request.data.get('password'))
        except ValidationError as error:
            raise RestValidationError(error)

        user_instance.set_password(request.data.get('password'))
        user_instance.save()

        return Response({'message': _('Password has been reset successfully')}, status=status.HTTP_200_OK)


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    search_field = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = RoleFilter
