from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 3:
            return True

# class IsReadAndManage(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.role == 2 or request.user.role == 3:
#             return True

class IsManage(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 1 or request.user.role == 2 or request.user.role == 3:
            return True

class IsRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 0 or request.user.role == 2 or request.user.role == 3:
            return True