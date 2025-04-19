from rest_framework import serializers

from appointment_system.user.models import AppointmentUser

class AppointmentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for AppointmentUser model.
    """
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = AppointmentUser
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }
    
    def update(self, instance, validated_data):
        validated_data.pop('password', None)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
