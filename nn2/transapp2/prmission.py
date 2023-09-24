from rest_framework.permissions import BasePermission

class TransPermission2(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id:
            return True
        
        return False