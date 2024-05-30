from django.db import models

from colors.models import Color
from ordered_model.models import OrderedModel


class Fruit(OrderedModel):
    name = models.CharField(max_length=20)
    color = models.ForeignKey(
        Color,
        blank=True,
        null=True,
        related_name="fruits",
        on_delete=models.CASCADE,
    )

    order_with_respect_to = ("name", "color")

    def __str__(self):
        return self.name
