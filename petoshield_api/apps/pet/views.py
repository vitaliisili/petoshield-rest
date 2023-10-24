from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.pet.models import Pet, Breed
from apps.pet.permissions import IsStaffOrOwner
from apps.pet.serializers import PetSerializer, BreedAdminSerializer, BreedSimpleSerializer


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = (IsStaffOrOwner,)

class BreedViewSet(viewsets.ModelViewSet):
    # serializer_class = BreedSimpleSerializer
    serializer_class = BreedAdminSerializer
    queryset = Breed.objects.all()
    permission_classes = (IsStaffOrOwner,)


    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return BreedAdminSerializer
    #     return BreedSimpleSerializer