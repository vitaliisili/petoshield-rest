from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from apps.core.utils import EmailSender
from apps.user.filters import RoleFilter, UserFilter
from apps.user.models import Role, MailVerificationTokens
from apps.user.permissions import UserPermission
from apps.user.serializers import BaseUserSerializer, ExtendUserSerializer, RoleSerializer, RegisterUserSerializer


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
        refresh = RefreshToken.for_user(user)
        EmailSender.send_confirmation_email(user, request.META.get('HTTP_REFERER'))

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def me(self, request):
        user_serializer = BaseUserSerializer(request.user)
        return Response(user_serializer.data, status=200)

    @action(detail=False, methods=['post'])
    def verify_email(self, request):

        mail_verification_token_instance = MailVerificationTokens.objects.filter(
            confirmation_token=request.data.get('token'))

        if not mail_verification_token_instance.exists():
            raise RestValidationError('Incorrect token')

        get_user_model().objects.filter(pk=mail_verification_token_instance[0].user.id).update(is_verified=True)
        return Response({'message': 'Thanks for verification'}, status=status.HTTP_200_OK)


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    search_field = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = RoleFilter
