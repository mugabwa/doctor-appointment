from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets

from appointment_system.common.permissions import IsPatientUser
from appointment_system.patient.models import (
    PatientContacts, PatientProfile)
from appointment_system.patient.serializers import (
    PatientContactSerializer, PatientProfileSerializer)

class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patient profile instances.
    """
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [IsPatientUser]
    authentication_classes = [OAuth2Authentication]
    filterset_fields = ['user__first_name', 'user__last_name', 'identifier']


class PatientContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patient contact instances.
    """
    queryset = PatientContacts.objects.all()
    serializer_class = PatientContactSerializer
    permission_classes = [IsPatientUser]
    authentication_classes = [OAuth2Authentication]
    filterset_fields = ['user__first_name', 'user__last_name', 'identifier']
