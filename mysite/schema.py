import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from colors.types import ColorListConnection
from fruits.types import FruitListConnection


@strawberry.type
class Query:
    colors: ColorListConnection = strawberry_django.connection()
    fruits: FruitListConnection = strawberry_django.connection()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)