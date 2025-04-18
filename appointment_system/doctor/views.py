from rest_framework import permissions, viewsets

from appointment_system.doctor.models import (
    DoctorContacts, DoctorProfile)
from appointment_system.doctor.serializers import (
    DoctorContactSerializer, DoctorProfileSerializer)


class DoctorProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing doctor profiles.
    """
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned profiles to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = self.queryset
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class DoctorContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing patient contact instances.
    """
    queryset = DoctorContacts.objects.all()
    serializer_class = DoctorContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['user__first_name', 'user__last_name', 'identifier']
