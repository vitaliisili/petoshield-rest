from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db import models
from apps.core.models import BaseModel


class Role(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.role = Role.objects.get(name='admin')
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, default=1, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_pictures', null=True)
    is_verified = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class MailVerificationTokens(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
