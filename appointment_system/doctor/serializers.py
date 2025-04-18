from rest_framework import serializers

from appointment_system.doctor.models import DoctorProfile, DoctorContacts

class DoctorProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the DoctorProfile model.
    """
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        read_only_fields = ('id', 'user')
        extra_kwargs = {
            'user': {'required': True},
            'identifier': {'required': True},
            'identifier_type': {'required': True},
        }

class DoctorContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contacts model.
    """
    class Meta:
        model = DoctorContacts
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'contact_type': {'required': True},
            'contact_value': {'required': True},
        }