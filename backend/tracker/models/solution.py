from django.db import models
from .problem import Problem


class Solution(models.Model):
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name="solutions"
    )
    language = models.CharField(max_length=30)
    code = models.TextField()
    explanation = models.TextField(blank=True)
    drawing = models.ImageField(upload_to="drawings/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solution for {self.problem.title} in {self.language}"
