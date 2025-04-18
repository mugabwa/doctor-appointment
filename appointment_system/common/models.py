from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

CONTACT_TYPE = (
    ('PHONE', 'Phone'),
    ('EMAIL', 'Email'),
)


class AbstractBaseModel(models.Model):
    """
    An abstract base model that provides common fields for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contacts(AbstractBaseModel):
    """
    Model representing a contact.
    """
    contact_value = models.CharField(max_length=255)
    contact_type = models.CharField(
        max_length=20, choices=CONTACT_TYPE, default='PHONE')
    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    contact_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name='contacts')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('contact_type', 'object_id')

    def __str__(self):
        return self.contact_value