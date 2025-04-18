from django.db import models

from appointment_system.common.models import (
    AbstractBaseModel, AbstractContacts)
from appointment_system.user.models import AppointmentUser


class PatientProfile(AbstractBaseModel):
    """
    A model to hold the patient information.
    """
    user = models.OneToOneField(
        AppointmentUser, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth = models.DateField(blank=True, null=True)
    identifier = models.CharField(max_length=255, unique=True)
    identifier_type = models.CharField(max_length=255)
    insurance_number = models.CharField(max_length=255, blank=True, null=True)
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class PatientContacts(AbstractContacts):
    """
    A model to hold the patient contact information.
    """
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name='contacts')
