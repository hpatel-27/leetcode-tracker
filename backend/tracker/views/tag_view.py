from rest_framework import viewsets, permissions
from ..models import Tag
from ..serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Tag instances.
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
