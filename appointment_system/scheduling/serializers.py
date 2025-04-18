from rest_framework import serializers

from appointment_system.scheduling.models import AppointmentScheduler

class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Appointment model.
    """
    class Meta:
        model = AppointmentScheduler
        fields = ['id', 'user', 'date', 'time', 'duration', 'status']
        read_only_fields = ['id', 'status']
