from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from appointment_system.user.models import AppointmentUser
from appointment_system.user.serializers import AppointmentUserSerializer

class AppointmentUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = AppointmentUser.objects.all()
    serializer_class = AppointmentUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
