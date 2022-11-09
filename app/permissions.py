from rest_framework import permissions
from rest_framework.response import Response



class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):
    # edit_methods = ("PUT")
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.type ==  "admin":
            return True
        else:
            return False            