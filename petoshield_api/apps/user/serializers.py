from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.user.models import Role, MailVerificationTokens


class RoleSerializer(serializers.ModelSerializer):
    """Serializer class for the Role model."""

    class Meta:
        """
        Attributes:
        model (Role): The model to be serialized.
        fields (str or list): The fields to include in the serialized representation.'__all__' includes all fields.
        read_only_fields (list): The fields that are read-only and should not be modified.
        """
        model = Role
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class BaseUserSerializer(serializers.ModelSerializer):
    """Base serializer for user models.
    Attributes:
        image (ImageField): The profile image of the user. Not required.
    Meta:
        model: The user model to be serialized.
        fields: The fields to be included in the serialized representation.
        read_only_fields: The fields that are read-only and cannot be modified.
    Methods:
        create: Creates and returns a new user instance.
    """

    image = serializers.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'image', 'is_verified']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        """Creates and returns a new user instance.
        Args:
            validated_data (dict): The validated data for creating the user.
        Returns:
            User: The newly created user instance.
        """

        validated_data['role'] = Role.objects.get(name='client')
        return get_user_model().objects.create_user(**validated_data)


class RegisterUserSerializer(BaseUserSerializer):
    """Serializer for registering new users.
    Meta:
        model: The user model to be serialized.
        fields: The fields to be included in the serialized representation.
    """

    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'password']


class ExtendUserSerializer(BaseUserSerializer):
    """Serializer for extending user information.
    Meta:
        model: The user model to be serialized.
        fields: The fields to be included in the serialized representation.
        extra_kwargs: Additional keyword arguments for field-level configuration.
        read_only_fields: The fields that are read-only and should not be modified.
    Methods:
        update: Updates the user instance with the validated data.
        to_representation: Convert the user instance to a representation, including the role name.
    """

    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        """Updates the user instance with the validated data.
        Args:
            instance: The user instance to be updated.
            validated_data: The validated data to be used for updating.
        Returns:
            User: The updated user instance.
        """

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def to_representation(self, instance):
        """Converts the user instance to a representation, including the role name.
        Args:
            instance: The user instance to be converted.
        Returns:
            dict: The representation of the user instance.
        """

        representation = super().to_representation(instance)
        representation['role'] = instance.role.name
        return representation


class EmailVerificationSerializer(serializers.ModelSerializer):
    """Serializer for email verification tokens.
    Meta:
        model (MailVerificationTokens): The model to be serialized.
        fields (list): The fields to be included in the serialized representation.
        read_only_fields (list): The fields that are read-only and should not be modified.
    """

    class Meta:
        model = MailVerificationTokens
        fields = ['id', 'user', 'confirmation_token']
        read_only_fields = ['id']


class ResetPasswordSerializer(serializers.Serializer):
    """Serializer for resetting password.
    Attributes:
        email (EmailField): The email address of the user. Required.
        redirect_link (URLField): The redirect link for password reset. Required.
    """

    email = serializers.EmailField(required=True)
    redirect_link = serializers.URLField(required=True)


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for changing password.
    Attributes:
        old_password (CharField): The old password of the user. Max length is 250 characters.
        new_password (CharField): The new password of the user. Max length is 150 characters.
    """

    old_password = serializers.CharField(max_length=250)
    new_password = serializers.CharField(max_length=150)
