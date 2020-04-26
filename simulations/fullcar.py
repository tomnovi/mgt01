# Create Concrete Factories
class Factory_FullCar(AbstractFactory):

    def create_suspensions(self) -> ConcreteSuspensions_FullCar:
        return ConcreteSuspensions_FullCar()

    def create_solvers(self) -> ConcreteSolvers_FullCar:
        return ConcreteSolvers_FullCar()

    def create_routines(self) -> ConcreteRoutines_FullCar:
        return ConcreteRoutines_FullCar()

    def create_postprocessors(self) -> ConcretePostprocessors_FullCar:
        return ConcretePostprocessors_FullCar()

# Create First Concrete Product
class Suspensions_FullCar(AbstractSuspensions):
    def useful_function_a(self) -> str:
        return "The result of the product FullCar."

# Create Second Concrete Product
class Solvers_FullCar(AbstractSolvers):
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
class Routines_FullCar(AbstractRoutines):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

# Create Fourth Concrete Product
class Postprocessors_FullCar(AbstractPostprocess):
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
