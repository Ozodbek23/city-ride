from rest_framework.permissions import BasePermission


class DriverPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return True
        return request.user.is_authenticated
