from rest_framework import permissions

class ProjectManagerPermission(permissions.BasePermission):
    """
    Custom permission to allow the unic project manager to act on project
    """

    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            