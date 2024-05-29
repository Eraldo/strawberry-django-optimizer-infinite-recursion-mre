from django.db import models

from colors.models import Color


class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.ForeignKey(
        Color,
        blank=True,
        null=True,
        related_name="fruits",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
