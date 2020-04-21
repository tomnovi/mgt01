import numpy as np
from utilities import rodrigues
import numpy as np

class Rack():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        self._trackrod_position = kwargs["trackrod"] if "trackrod" in kwargs else None

    # Set new rack position based on rack displacement
    def set_rack_position(self, rack_displacement):
        # Define local variables in scope of function
        trackrod_position = self._trackrod_position

        # Apply rack displacement, this is simply a displacement along the y axis
        self._trackrod_position = trackrod_position + np.array([0, rack_displacement, 0])

    # Get rack position
    def get_rack_position(self):
        trackrod_position = self._trackrod_position
        return trackrod_position

    # Update Rock position
    def update(self, rack_displacement):
        # Update rack position
        self.set_rack_position(rack_displacement)
