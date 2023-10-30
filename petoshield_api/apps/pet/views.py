from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.pet.models import Pet, Breed
from apps.pet.permissions import IsStaffOrOwner
from apps.pet.serializers import PetSerializer, BaseBreedSerializer, ExtendBreedSerializer, PetUserCombinedSerializer
from apps.user.models import Role


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated, IsStaffOrOwner)
    search_fields = ['$name']
    ordering_fields = ['created_at', 'name', 'gender', 'species', 'age']

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

    @action(methods=['post'], detail=False)
    def create_new_account(self, request, pk=None):
        serializer = PetUserCombinedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user['role'] = Role.objects.get(name='client')
        user_instance = get_user_model().objects.create_user(**user)

        pet = serializer.validated_data['pet']
        pet['user'] = user_instance
        Pet.objects.create(**pet)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Pet.objects.filter(user=self.request.user)
        return Pet.objects.all()


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrOwner)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ExtendBreedSerializer
        return BaseBreedSerializer
