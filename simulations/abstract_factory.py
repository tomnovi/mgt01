
from __future__ import annotations
from abc import ABC, abstractmethod

# Create Abstract Factory
class AbstractFactory():

    @abstractmethod
    def create_suspensions(self) -> AbstractSuspensions:
        pass

    @abstractmethod
    def create_solvers(self) -> AbstractSolvers:
        pass

    @abstractmethod
    def create_routines(self) -> AbstractRoutines:
        pass

    @abstractmethod
    def create_postprocessors(self) -> AbstractPostprocess:
        pass

# Create First Product
class AbstractSuspensions():

    @abstractmethod
    def useful_function_a(self) -> str:
        pass

# Create Second Product
class AbstractSolvers():

    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass

# Create Third Product
class AbstractRoutines():

    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass

# Create Fourth Product
class AbstractPostprocess():

    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass
