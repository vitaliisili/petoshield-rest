from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.pet.models import Pet, Breed
from apps.pet.permissions import IsStaffOrOwner
from apps.pet.serializers import PetSerializer, BaseBreedSerializer, ExtendBreedSerializer


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrOwner)
    search_fields = ['$name']
    ordering_fields = ['created_at', 'name', 'gender', 'species', 'age']

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrOwner)
    search_fields = ['$name']
    ordering_fields = ['name', 'created_at']

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ExtendBreedSerializer
        return BaseBreedSerializer
