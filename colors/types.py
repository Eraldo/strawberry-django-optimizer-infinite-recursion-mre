from typing import List, Optional, Annotated, TYPE_CHECKING

import strawberry
from strawberry import auto

import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount

from . import models

if TYPE_CHECKING:
    from fruits.types import FruitListConnection

@strawberry_django.filters.filter(models.Color, lookups=True)
class ColorFilter:
    id: auto
    name: auto


@strawberry_django.ordering.order(models.Color)
class ColorOrder:
    name: auto


@strawberry_django.type(
    models.Color,
    filters=ColorFilter,
    order=ColorOrder,
)
class Color(Node):
    name: auto
    fruits: Annotated["FruitListConnection", strawberry.lazy("fruits.types")] = strawberry_django.connection()


ColorListConnection = ListConnectionWithTotalCount[Color]