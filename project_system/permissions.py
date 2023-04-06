from rest_framework import permissions


class HasAInUsername(permissions.BasePermission):
    message = {"success": False,
               "message": "You don't have permission to access this page. There is no letter 'Y' in your username"}

    def has_permission(self, request, view):
        if request.user.username.__contains__("y"):
            return True
        return False
