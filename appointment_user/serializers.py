from rest_framework import serializers

from appointment_user.models import AppointmentUser

class AppointmentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for AppointmentUser model.
    """
    class Meta:
        model = AppointmentUser
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }