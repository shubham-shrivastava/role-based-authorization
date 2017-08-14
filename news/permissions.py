from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, obj):
        if "Admin" in request.user.groups.values_list('name',flat=True) or request.user.is_superuser:
            return True
        else:
            return False

class CanChangeArticle(permissions.BasePermission):
    def has_permission(self, request, obj):
        if "Subscriber" in request.user.groups.values_list('name',flat=True) and request.method != "GET":
            return False
        else:
            return True


class IsAdminOrEditor(permissions.BasePermission):
    def has_permission(self, request, obj):
        if "Admin" in request.user.groups.values_list('name',flat=True) or request.user.is_superuser or "Editor" in request.user.groups.values_list('name',flat=True):
            return True
        else:
            return False


class OnlyUser(permissions.BasePermission):
    def has_permission(self, request, obj):
        if request.user is None:
            return False
        else:
            return True