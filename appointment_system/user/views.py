from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import viewsets, permissions

from appointment_system.common.permissions import (
    IsAdminOrReceptionistUser, IsAdminOrSelf)
from appointment_system.user.models import AppointmentUser
from appointment_system.user.serializers import AppointmentUserSerializer

class AppointmentUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = AppointmentUser.objects.all()
    serializer_class = AppointmentUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf, IsAdminOrReceptionistUser]
    authentication_classes = [OAuth2Authentication]
