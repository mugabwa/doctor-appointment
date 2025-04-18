from rest_framework import routers

from appointment_system.patient.views import (
    PatientContactViewSet, PatientProfileViewSet)

router = routers.SimpleRouter()

router.register(
    r'patient_profiles',
    PatientProfileViewSet,
    basename='patient_profile',
)
router.register(
    r'patient_contacts',
    PatientContactViewSet,
    basename='patient_contact',
)

urlpatterns = router.urls