from rest_framework import serializers

from appointment_system.patient.models import (
    Contacts, PatientProfile)

class PatientProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the PatientProfile model.
    """
    class Meta:
        model = PatientProfile
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'identifier': {'required': True},
            'identifier_type': {'required': True},
        }


class PatientContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contacts model.
    """
    class Meta:
        model = Contacts
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'contact_type': {'required': True},
            'contact_value': {'required': True},
        }
