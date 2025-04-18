from django.db import models

from appointment_system.doctor.models import DoctorProfile
from appointment_system.patient.models import PatientProfile

APPOINTMENT_STATUS = (
    ('SCHEDULED', 'Scheduled'),
    ('RESCHEDULED', 'Rescheduled'),
    ('CANCELLED', 'Cancelled'),
    ('NO_SHOW', 'No Show'),
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('IN_PROGRESS', 'In Progress'),
    ('COMPLETED', 'Completed'),
    ('CANCELLED', 'Cancelled'),
)

class AppointmentScheduler(models.Model):
    """
    A model to hold the appointment scheduling information.
    """
    appointment_date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=APPOINTMENT_STATUS, default='SCHEDULED')

    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.appointment_date} {self.appointment_time}"
