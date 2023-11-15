import uuid
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.core.utils import EmailSender, JwtToken
from apps.pet.models import Pet, Breed
from apps.pet.permissions import BreedPermissions, PetPermission
from apps.pet.serializers import PetSerializer, BaseBreedSerializer, ExtendBreedSerializer, PetUserCombinedSerializer
from apps.pet.filters import BreedFilter, PetFilter
from apps.policy.models import Policy
from apps.user.models import Role
from datetime import date
from apps.policy import utils
from config import settings


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = (PetPermission,)
    search_fields = ['$name']
    ordering_fields = ['created_at', 'name', 'gender', 'species', 'age']
    ordering = ['-created_at']
    filterset_class = PetFilter

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            request.data['user'] = request.user.id

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        pet_instance = serializer.save()

        Policy.objects.create(
            policy_number=uuid.uuid4(),
            start_date=date.today(),
            end_date=date.today().replace(year=date.today().year + 1),
            initial_limit=settings.POLICY_INITIAL_LIMIT,
            current_limit=settings.POLICY_INITIAL_LIMIT,
            deductible=settings.POLICY_DEDUCTIBLE,
            status='invalid',
            pet=pet_instance,
            price=utils.get_policy_price(pet_instance)
        )

        response = JwtToken.get_jwt_token(request.user)
        response['pet'] = pet_instance.id

        return Response(response, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            request.data['user'] = request.user.id
        return super().update(request, *args, **kwargs)

    @action(methods=['post'], detail=False)
    def create_new_account(self, request, pk=None):
        serializer = PetUserCombinedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        user['role'] = Role.objects.get(name='client')
        user_instance = get_user_model().objects.create_user(**user)

        pet = serializer.validated_data['pet']
        pet['user'] = user_instance
        pet_instance = Pet.objects.create(**pet)

        Policy.objects.create(
            policy_number=uuid.uuid4(),
            start_date=date.today(),
            end_date=date.today().replace(year=date.today().year + 1),
            initial_limit=settings.POLICY_INITIAL_LIMIT,
            current_limit=settings.POLICY_INITIAL_LIMIT,
            deductible=settings.POLICY_DEDUCTIBLE,
            status='invalid',
            pet=pet_instance,
            price=utils.get_policy_price(pet_instance)
        )

        EmailSender.send_welcome_email(user_instance)
        EmailSender.send_confirmation_email(user_instance, request.META.get('HTTP_REFERER'))

        response = JwtToken.get_jwt_token(user_instance)
        response['pet'] = pet_instance.id

        return Response(response, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Pet.objects.filter(user=self.request.user)
        return Pet.objects.all()


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    permission_classes = (BreedPermissions,)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']
    filterset_class = BreedFilter

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ExtendBreedSerializer
        return BaseBreedSerializer
