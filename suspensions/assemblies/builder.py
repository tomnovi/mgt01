from __future__ import annotations
from abc import abstractmethod, abstractproperty

# Create Builder Interface
class Builder():

    @abstractproperty
    def product(self) -> None:
        pass

    #@abstractmethod
    #def define_pickups(self) -> None:
    #    pass

    @abstractmethod
    def produce_wheel(self) -> None:
        pass

    @abstractmethod
    def produce_elasticlinks(self) -> None:
        pass

    @abstractmethod
    def produce_rigidlinks(self) -> None:
        pass

# Create Product Class
class Suspensions():

    def __init__(self) -> None:
        self.parts = {}

    def add(self, **kwargs) -> None:
        self.parts.update(kwargs)


# Create Director Class
class Director():
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        # The Director works with any builder instance that the client code passes
        # to it. This way, the client code may alter the final type of the newly
        # assembled product.
        self._builder = builder

    # The Director can construct several product variations using the same
    # building steps.
    def build_simplified_suspension(self) -> None:
        self.builder.produce_wheel()

    def build_full_suspension(self) -> None:
        self.builder.produce_wheel()
        self.builder.produce_elasticlinks()
        self.builder.produce_rigidlinks()
