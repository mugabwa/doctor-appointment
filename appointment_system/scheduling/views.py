from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets

from appointment_system.common.permissions import (
    IsAdminOrDoctorUser, IsAdminOrReceptionistUser,
    IsPatientUser)
from appointment_system.scheduling.models import AppointmentScheduler
from appointment_system.scheduling.serializers import AppointmentSerializer

class AppointmentSchedulerViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing appointment scheduling.
    """
    queryset = AppointmentScheduler.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsPatientUser, IsAdminOrDoctorUser, IsAdminOrReceptionistUser]

    def get_queryset(self):
        """
        Optionally restricts the returned appointments to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = self.queryset
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset