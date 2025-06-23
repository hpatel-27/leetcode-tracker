from rest_framework import serializers
from ..models import Problem, Tag
from .solution_serializer import SolutionSerializer


class ProblemSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True, queryset=Tag.objects.all(), slug_field="name"
    )
    solutions = SolutionSerializer(many=True, read_only=True)

    class Meta:
        model = Problem
        fields = [
            "id",
            "title",
            "url",
            "status",
            "difficulty",
            "tags",
            "solutions",
            "solved_at",
        ]
        read_only_fields = ["solved_at"]
