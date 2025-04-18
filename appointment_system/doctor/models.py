from django.db import models

from appointment_system.common.models import (
    AbstractBaseModel, AbstractContacts)
from appointment_system.user.models import AppointmentUser

DOCTOR_AVAILABILITY_STATUS = (
    ('AVAILABLE', 'Available'),
    ('UNAVAILABLE', 'Unavailable'),
    ('ON_LEAVE', 'On Leave'),
    ('BUSY', 'Busy'),
)

DOCTOR_IDENTIFIER_TYPE = (
    ('NATIONAL_ID', 'National ID'),
    ('LICENSE_NUMBER', 'License Number'),
    ('PASSPORT', 'Passport'),
    ('REGISTRATION_NUMBER', 'Registration Number'),
)

class DoctorProfile(AbstractBaseModel):
    """
    A model to hold the doctor information.
    """
    user = models.OneToOneField(
        AppointmentUser, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class DoctorContacts(AbstractContacts):
    """
    A model to hold the doctor contact information.
    """
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.contact_value


class DoctorIdentifier(AbstractBaseModel):
    """
    A model to hold the doctor's identifier information.
    """
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name='identifiers')
    identifier = models.CharField(max_length=255, unique=True)
    identifier_type = models.CharField(max_length=255, choices=DOCTOR_IDENTIFIER_TYPE)

    def __str__(self):
        return f"{self.doctor.user.first_name} {self.doctor.user.last_name} - {self.identifier}"


class DoctorAvialibility(AbstractBaseModel):
    """
    A model to hold the doctor's availability information.
    """
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name='availability')
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(
        max_length=20, choices=DOCTOR_AVAILABILITY_STATUS, default='AVAILABLE')

    def __str__(self):
        return f"{self.doctor.user.first_name} {self.doctor.user.last_name} - {self.day_of_week}"
