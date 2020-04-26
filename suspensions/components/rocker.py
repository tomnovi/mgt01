import numpy as np
from utilities import rodrigues

class Rocker():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        self.rocker_travel = 0

    # Property for rocker angle
    @property
    def rocker_angle(self):
        return self._rocker_angle

    # Setter for rocker angle
    @rocker_angle.setter
    def rocker_angle(self, value):
        # Apply rodrigues rotation
        self._rocker_angle = value
