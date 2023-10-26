from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from apps.user.permissions import UserPermission
from apps.user.serializers import BaseUserSerializer, ExtendUserSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (UserPermission,)
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'created_at']

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ExtendUserSerializer
        return BaseUserSerializer