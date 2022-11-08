from rest_framework import permissions



class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):


    # edit_methods = ("PUT")

    def has_permission(self, request):
        if request.user.is_authenticated and request.user.type ==  "admin":
            return True
        else:
            return False            