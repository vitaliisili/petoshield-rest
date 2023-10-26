from rest_framework import serializers
from apps.pet.models import Pet, Breed


class PetSerializer(serializers.ModelSerializer):
    class Meta:
       model = Pet
       fields = '__all__'
       read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['breed'] = instance.breed.name
        return representation

class BaseBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'description', 'species']
        read_only_fields = ['id']

class ExtendBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
        read_only_fields = ['id']