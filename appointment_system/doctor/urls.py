from rest_framework import routers

from appointment_system.doctor.views import (
    DoctorContactViewSet, DoctorProfileViewSet)

router = routers.SimpleRouter()

router.register(
    r'doctor_profiles',
    DoctorProfileViewSet,
    basename='doctor_profile',
)
router.register(
    r'doctor_contacts',
    DoctorContactViewSet,
    basename='doctor_contact',
)

urlpatterns = router.urls