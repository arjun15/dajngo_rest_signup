"""
Permission class for authorized user
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        check user login
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
