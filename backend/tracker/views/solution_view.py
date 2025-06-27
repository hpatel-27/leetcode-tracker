from rest_framework import viewsets, permissions
from ..models import Solution
from ..serializers import SolutionSerializer


class SolutionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Solution instances.
    """

    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned solutions to those owned by the requesting user,
        by filtering against a `username` query parameter in the URL.
        """
        return Solution.objects.filter(user=self.request.user)