from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from appointment_system.patient.models import (
    Contacts, PatientProfile)
from appointment_system.patient.serializers import (
    PatientContactSerializer, PatientProfileSerializer)

class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patient profile instances.
    """
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filterset_fields = ['user__first_name', 'user__last_name', 'identifier']


class PatientContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patient contact instances.
    """
    queryset = Contacts.objects.all()
    serializer_class = PatientContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filterset_fields = ['user__first_name', 'user__last_name', 'identifier']
