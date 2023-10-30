from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.user.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name']
        read_only_fields = ['id']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class ExtendUserSerializer(BaseUserSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['role'] = instance.role.name
        return representation
