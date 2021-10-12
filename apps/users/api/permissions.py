from rest_framework.permissions import IsAdminUser


class IsAdminUserCustom(IsAdminUser):
    """
    Instantiates and returns the list of required permissions.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return super().has_permission(request, view)
