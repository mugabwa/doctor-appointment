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


class AbstractContacts(AbstractBaseModel):
    """
    Model representing a contact.
    """
    contact_value = models.CharField(max_length=255)
    contact_type = models.CharField(
        max_length=20, choices=CONTACT_TYPE, default='PHONE')
    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.contact_value

    class Meta:
        abstract = True
