# Create Concrete Builders
class MacPherson(Builder):

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

    def produce_wheel(self) -> None:
        self._product.add("Wheel")

    def produce_elasticlinks(self) -> None:
        self._product.add("Spring")

    def produce_rigidlinks(self) -> None:
        self._product.add("Links")
