from django.db import models
from django.contrib.auth.models import User
from .tag import Tag


class Problem(models.Model):

    class Difficulty(models.TextChoices):
        EASY = "Easy", "Easy"
        MEDIUM = "Medium", "Medium"
        HARD = "Hard", "Hard"

    class Status(models.TextChoices):
        NOT_STARTED = "Not Started", "Not Started"
        ATTEMPTED = "Attempted", "Attempted"
        SOLVED = "Solved", "Solved"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NOT_STARTED
    )
    difficulty = models.CharField(
        max_length=10, choices=Difficulty.choices, default=Difficulty.EASY
    )
    tags = models.ManyToManyField(Tag, blank=True)
    solved_at = models.DateTimeField(null=True, blank=True)
