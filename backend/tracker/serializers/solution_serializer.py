from rest_framework import serializers
from ..models import Solution
from .solution_serializer import SolutionSerializer
from ..models import Tag


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = [
            "id",
            "problem",
            "language",
            "code",
            "explanation",
            "drawing",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at"]
