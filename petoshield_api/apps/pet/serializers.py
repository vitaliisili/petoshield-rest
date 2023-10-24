from rest_framework import serializers
from apps.pet.models import Pet, Breed


class PetSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pet
       fields = '__all__'
       read_only_fields = ['id']

class BreedSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'description', 'species']
        read_only_fields = ['id']

class BreedAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
        read_only_fields = ['id']