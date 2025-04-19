from rest_framework.permissions import BasePermission

class HasRolePermission(BasePermission):
    """
    Custom permission to check if the user has a specific role.
    """
    required_roles = []

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Get the required role from the view
        required_role = getattr(view, 'required_role', None)
        if required_role is None:
            return True  # No specific role required

        # Check if the user's role matches the required role
        return request.user.role.name == required_role


class IsAdminUser(HasRolePermission):
    """
    Custom permission to check if the user is an admin.
    """
    required_roles = ['ADMIN']

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsDoctorUser(HasRolePermission):
    """
    Custom permission to check if the user is a doctor.
    """
    required_roles = ['DOCTOR']

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsPatientUser(HasRolePermission):
    """
    Custom permission to check if the user is a patient.
    """
    required_roles = ['PATIENT']

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsReceptionistUser(HasRolePermission):
    """
    Custom permission to check if the user is a receptionist.
    """
    required_roles = ['RECEPTIONIST']

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsAdminOrDoctorUser(HasRolePermission):
    """
    Custom permission to check if the user is an admin or a doctor.
    """
    required_roles = ['ADMIN', 'DOCTOR']

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsAdminOrReceptionistUser(HasRolePermission):
    """
    Custom permission to check if the user is an admin or a receptionist.
    """
    required_roles = ['ADMIN', 'RECEPTIONIST']

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class IsAdminOrSelf(BasePermission):
    """
    Custom permission to check if the user is an admin or the object owner.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is an admin
        if request.user.role and request.user.role.name == 'ADMIN':
            return True

        # Check if the user is the object owner
        obj = view.get_object()
        return obj == request.user
