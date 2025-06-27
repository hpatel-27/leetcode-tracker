from rest_framework import viewsets, permissions
from ..models import Problem
from ..serializers import ProblemSerializer
from django.db.models.query import QuerySet


class ProblemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Problem instances.
    """

    serializer_class = ProblemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned problems to those owned by the requesting user,
        by filtering against a `username` query parameter in the URL.
        """
        return Problem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the user as the owner of the problem when creating a new problem.
        """
        serializer.save(user=self.request.user)
