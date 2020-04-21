import numpy as np
from utilities import rodrigues

class Rocker():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        # Define public attributes
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None
        self.pushrod_position = kwargs["pushrod"] if "pushrod" in kwargs else None
        self.damper_position = kwargs["damper"] if "damper" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None

        # Instiate rodrigues objects
        self.pushrod_rotation = rodrigues.Rodrigues(pivot_position=self.pivot_position, pickup_position=self.pushrod_position, rotation_axis=self.rocker_axis)
        self.damper_rotation = rodrigues.Rodrigues(pivot_position=self.pivot_position, pickup_position=self.damper_position, rotation_axis=self.rocker_axis)

        # Define private attributes
        self._rocker_angle = 0
        self._drocker_angle = 0

    # Property for rocker angle
    @property
    def rocker_angle(self):
        return self._rocker_angle

    # Setter for rocker angle
    @rocker_angle.setter
    def rocker_angle(self, value):
        # Apply rodrigues rotation
        self._drocker_angle = value

    # Rotation to pushrod
    def apply_rotation(self):
        self._rocker_angle += self._drocker_angle
        self.pushrod_position = self.pushrod_rotation.rotation(self._drocker_angle)
        self.damper_position = self.damper_rotation.rotation(self._drocker_angle)
        self.dpushrod_drocker = self.pushrod_rotation.first_derivative(self._drocker_angle)
        self.ddamper_drocker = self.damper_rotation.first_derivative(self._drocker_angle)
