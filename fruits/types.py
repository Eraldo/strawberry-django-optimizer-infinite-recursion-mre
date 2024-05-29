from strawberry import auto

import strawberry_django
from strawberry.relay import Node
from strawberry_django.relay import ListConnectionWithTotalCount

from . import models


@strawberry_django.filters.filter(models.Fruit, lookups=True)
class FruitFilter:
    id: auto
    name: auto


@strawberry_django.ordering.order(models.Fruit)
class FruitOrder:
    name: auto


@strawberry_django.type(
    models.Fruit,
    filters=FruitFilter,
    order=FruitOrder,
)
class Fruit(Node):
    name: auto


FruitListConnection = ListConnectionWithTotalCount[Fruit]
