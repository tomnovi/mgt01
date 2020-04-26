# Create Concrete Factories
class Factory_HalfCar(AbstractFactory):

    def create_suspensions(self) -> ConcreteSuspensions_HalfCar:
        return ConcreteSuspensions_HalfCar()

    def create_solvers(self) -> ConcreteSolvers_HalfCar:
        return ConcreteSolvers_HalfCar()

    def create_routines(self) -> ConcreteRoutines_HalfCar:
        return ConcreteRoutines_HalfCar()

    def create_postprocessors(self) -> ConcretePostprocessors_HalfCar:
        return ConcretePostprocessors_HalfCar()

# Create First Concrete Product
class Suspensions_HalfCar(AbstractSuspensions):
    def useful_function_a(self) -> str:
        return "The result of the product HalfCar."

# Create Second Concrete Product
class Solvers_HalfCar(AbstractSolvers):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"

# Create Third Concrete Product
class Routines_HalfCar(AbstractRoutines):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

# Create Fourth Concrete Product
class Postprocessors_HalfCar(AbstractPostprocess):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
