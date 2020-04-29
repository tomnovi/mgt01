from .builder import Suspensions, Builder
from ..components.wheel import Wheel
from ..components.spring import Spring
from ..components.rack import Rack
from ..components.prod import Prod

# Create Concrete Builders
class DoubleWishbone(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Suspensions()

    @property
    def product(self) -> Suspensions:
        # We reset the product after having ceated it so the builder is ready
        # for creating another instance
        product = self._product
        self.reset()
        return product

    #def define_pickups(self) -> None:
    #    pass

    def produce_wheel(self) -> None:
        self._product.add(wheel=Wheel())

    def produce_elasticlinks(self) -> None:
        self._product.add(spring=Spring())

    def produce_rigidlinks(self) -> None:
        self._product.add(prod=Prod(), rack=Rack())
