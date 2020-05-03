import numpy as np
from utilities import rodrigues

class Rocker():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        # Rocker
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None        # Define public attributes
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None
        self.rocker_travel = 0
        # Pushrod
        self.prod_position = kwargs["prod"] if "prod" in kwargs else None
        self.prod_rotation = rodrigues.Rodrigues(pivot_position=self.pivot_position, pickup_position=self.prod_position, rotation_axis=self.rocker_axis)
        # Damper
        self.damper_position = kwargs["damper"] if "damper" in kwargs else None
        self.damper_rotation = rodrigues.Rodrigues(pivot_position=self.pivot_position, pickup_position=self.damper_position, rotation_axis=self.rocker_axis)

    # Property for rocker angle
    @property
    def rocker_angle(self):
        return self._rocker_angle

    # Setter for rocker angle
    @rocker_angle.setter
    def rocker_angle(self, value):
        # Apply rodrigues rotation
        self._rocker_angle = value

    # Rotation to pushrod
    def apply_rotation(self):
        # Apply rocker rotation
        self.rocker_travel += self._rocker_angle
        # Find pushrod position after rotation
        self.prod_position = self.prod_rotation.rotation(self._rocker_angle)
        self.dpushrod_drocker = self.prod_rotation.first_derivative(self._rocker_angle)
        # Find damper position after rotation
        self.damper_position = self.damper_rotation.rotation(self._rocker_angle)
        self.ddamper_drocker = self.damper_rotation.first_derivative(self._rocker_angle)
