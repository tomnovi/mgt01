# Create Builder Interface
class Builder():

    def product(self):
        pass

    def read_pickups(self):
        pass

    def produce_wheel(self):
        pass

    def produce_elasticlinks(self):
        pass

    def produce_rigidlinks(self):
        pass

# Create Product Class
class Suspensions():

    def __init__(self):
        self.parts = {}
        self.points = {}

    def read(self, **kwargs):
        self.points.update(kwargs)

    def add(self, **kwargs):
        self.parts.update(kwargs)


# Create Director Class
class Director():
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        # The Director works with any builder instance that the client code passes
        # to it. This way, the client code may alter the final type of the newly
        # assembled product.
        self._builder = builder

    # The Director can construct several product variations using the same
    # building steps.
    def build_simplified_suspension(self):
        self.builder.read_pickups()
        self.builder.produce_wheel()

    def build_full_suspension(self):
        self.builder.read_pickups()
        self.builder.produce_wheel()
        self.builder.produce_elasticlinks()
        self.builder.produce_rocker()
        self.builder.produce_rack()
