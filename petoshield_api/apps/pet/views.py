from rest_framework import viewsets
from apps.pet.models import Pet, Breed
from apps.pet.permissions import IsStaffOrOwner
from apps.pet.serializers import PetSerializer, BreedAdminSerializer, BreedSimpleSerializer

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsStaffOrOwner,)
    search_fields = ['name', 'type']  # Example fields for search
    ordering_fields = ['created_at', 'name']  # Example fields for ordering
    ordering = ['created_at']

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    permission_classes = (IsStaffOrOwner,)
    search_fields = ['name']  # Example fields for search
    ordering_fields = ['name']  # Example fields for ordering
    ordering = ['name']

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return BreedAdminSerializer
        return BreedSimpleSerializer

