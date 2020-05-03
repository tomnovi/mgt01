from .builder import Suspensions, Builder
from ..components.wheel import Wheel
from ..components.spring import Spring
from ..components.rack import Rack
from ..components.prod import Prod
from ...data.suspensions import pickups

# Create Concrete Builders
class DoubleWishbone(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Suspensions()

    @property
    def product(self):
        # We reset the product after having ceated it so the builder is ready
        # for creating another instance
        product = self._product
        self.reset()
        return product

    #def define_pickups(self) -> None:
    #    pass
    def read_pickups(self):
        self._product.read()

    def produce_wheel(self):
        self._product.add(wheel=Wheel())

    def produce_elasticlinks(self):
        self._product.add(spring=Spring())

    def produce_rocker(self):
        self._product.add(rocker=Rocker(), rack=Rack())
