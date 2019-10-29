from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing users.

    GET /users/
    :returns a list of all users

    GET user/id/
    :returns a user by id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
