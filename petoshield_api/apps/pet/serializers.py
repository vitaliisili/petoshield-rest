from rest_framework import serializers
from apps.pet.models import Pet, Breed
from apps.policy.serializers import PolicySerializer
from apps.user.serializers import RegisterUserSerializer


class PetSerializer(serializers.ModelSerializer):
    policy = PolicySerializer(read_only=True, many=True)

    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['breed'] = instance.breed.name

        policy = instance.policy.first()
        representation['policy'] = PolicySerializer(policy).data if policy else None

        return representation


class ExtendPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ['user']
        read_only_fields = ['id']


class PetUserCombinedSerializer(serializers.Serializer):
    user = RegisterUserSerializer()
    pet = ExtendPetSerializer()


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
