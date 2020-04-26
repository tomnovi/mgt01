class Director():
    # Director - It refers to Builder abstract class to build the products
    def __init__(self, builder):
        self._builder = builder

    def construct_sim(self):
        self._builder.create_new_simulation()
        self._builder.add_suspensions()
        self._builder.add_solvers()
        self._builder.add_routines()
        self._builder.add_postprocess()


    def get_sim(self):
        return self._builder.sim


class Builder():
    # Abstract builder
    def __init__(self):
        self.sim = None

    def create_new_simulation(self):
        self.sim = Simulation()



class Simulation():
    # Product
    def __init__(self):
        self.suspensions = None
        self.solvers = None
        self.routines = None
        self.postprocess = None


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)
