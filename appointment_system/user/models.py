from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

USER_ROLES = (
    ('DOCTOR', 'Doctor'),
    ('PATIENT', 'Patient'),
    ('ADMIN', 'Admin'),
    ('RECEPTIONIST', 'Receptionist'),
)

GENDER_CHOICES = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class AppointmentUser(AbstractBaseUser, PermissionsMixin):
    """
    A model to hold the user information for the appointment system.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(
        max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(
        max_length=50, choices=USER_ROLES, default='PATIENT'
    )
    gender = models.CharField(
        max_length=15, choices=GENDER_CHOICES, default='OTHER'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.ForeignKey(
        'Role', on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Role(models.Model):
    """
    A model containing the roles assigned to each user.
    """
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField('Permission', blank=True)

    def __str__(self):
        return self.name
    

class Permission(models.Model):
    """
    A model containing the permissions assigned to each role.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
