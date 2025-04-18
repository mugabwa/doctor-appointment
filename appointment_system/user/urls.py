from rest_framework import routers

from appointment_system.user.views import AppointmentUserViewSet

router = routers.SimpleRouter()

router.register(
    r'users',
    AppointmentUserViewSet,
    basename='user',
)

urlpatterns = router.urls