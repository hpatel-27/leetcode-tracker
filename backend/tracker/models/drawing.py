from django.db import models
from .solution import Solution


class Drawing(models.Model):
    solution = models.ForeignKey(
        Solution, on_delete=models.CASCADE, related_name="drawings"
    )
    image = models.ImageField(upload_to="drawings/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Drawing for {self.solution.problem.title}"
