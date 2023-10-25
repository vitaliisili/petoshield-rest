from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from apps.user.permissions import UserPermission
from apps.user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (UserPermission,)
    search_fields = ['username', 'email']  # Example fields for search
    ordering_fields = ['username', 'date_joined']  # Example fields for ordering
    ordering = ['date_joined']