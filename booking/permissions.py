from rest_framework import permissions


class CheckRole(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.profile.user_role == 'owner':
            return True
        if request.user.profile.user_role == 'customer':
            return True
        return False


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.booking_hotel.owner != request.user


class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False