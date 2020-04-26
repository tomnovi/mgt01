# Create Concrete Factories
class Factory_QuarterCar(AbstractFactory):

    def create_suspensions(self) -> ConcreteSuspensions_QuarterCar:
        return ConcreteSuspensions_QuarterCar()

    def create_solvers(self) -> ConcreteSolvers_QuarterCar:
        return ConcreteSolvers_QuarterCar()

    def create_routines(self) -> ConcreteRoutines_QuarterCar:
        return ConcreteRoutines_QuarterCar()

    def create_postprocessors(self) -> ConcretePostprocessors_QuarterCar:
        return ConcretePostprocessors_QuarterCar()

# Create First Concrete Product
class Suspensions_QuarterCar(AbstractSuspensions):
    def useful_function_a(self) -> str:
        return "The result of the product QuarterCar."

# Create Second Concrete Product
class Solvers_QuarterCar(AbstractSolvers):
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
class Routines_QuarterCar(AbstractRoutines):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

# Create Fourth Concrete Product
class Postprocessors_QuarterCar(AbstractPostprocess):
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
