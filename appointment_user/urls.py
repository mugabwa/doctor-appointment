from rest_framework import routers

from appointment_user.views import AppointmentUserViewSet

router = routers.SimpleRouter()

router.register(
    r'users',
    AppointmentUserViewSet,
    basename='user',
)

urlpatterns = router.urls