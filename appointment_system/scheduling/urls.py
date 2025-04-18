from rest_framework import routers

from appointment_system.scheduling.views import (
    AppointmentSchedulerViewSet)

router = routers.SimpleRouter()

router.register(
    r'schedule_appointments',
    AppointmentSchedulerViewSet,
    basename='schedule_appointments',
)

urlpatterns = router.urls