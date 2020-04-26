import numpy as np

class Rack():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        self.trackrod_position = kwargs["trackrod"] if "trackrod" in kwargs else None
        self.rack_travel = 0

    # Property for rack displacement
    @property
    def rack_displacement(self):
        return self._drack_displacement

    # Setter for rack displacement
    @rack_displacement.setter
    def rack_displacement(self, value):
        self._drack_displacement = value

    # Set new rack position based on rack displacement
    def apply_displacement(self):
        # Define local variables in scope of function
        self.rack_travel += self._drack_displacement
        # Apply rack displacement, this is simply a displacement along the y axis
        self.trackrod_position = self.trackrod_position + np.array([0, self._drack_displacement, 0])
        # Apply derivative or trackrod position wrt to rack rack_displacement
        self.dtrackrod_drack = np.array([0, 1, 0])
