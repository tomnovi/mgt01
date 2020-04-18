import numpy as np
from utilities import rodrigues

class Rocker():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        self._pivot_position = kwargs["pivot"] if "pivot" in kwargs else None
        self._pushrod_position = kwargs["pushrod"] if "pushrod" in kwargs else None
        self._damper_position = kwargs["damper"] if "damper" in kwargs else None
        self._axis1_position = kwargs["axis1"] if "axis1" in kwargs else None
        self._axis2_position = kwargs["axis2"] if "axis2" in kwargs else None
        rocker_axis = self._axis1_position - self._axis2_position
        self._rocker_axis = rocker_axis / np.linalg.norm(rocker_axis)

    # Set new pushrod position based on rocker rotation
    def set_pushrod_position(self, rocker_angle):
        # Define local variables in scope of function
        pushrod_position = self._pushrod_position
        pivot_position = self._pivot_position
        rocker_axis = self._rocker_axis

        # Apply rodrigues rotation
        self._pushrod_position = rodrigues.rodrigues_rotation(pushrod_position, pivot_position, rocker_axis, rocker_angle)

    # Set new dmaper position based on rocker rotation
    def set_damper_position(self, rocker_angle):
        # Define local variables in scope of function
        damper_position = self._damper_position
        pivot_position = self._pivot_position
        rocker_axis = self._rocker_axis

        # Apply rodrigues rotation
        self._damper_position = rodrigues.rodrigues_rotation(damper_position, pivot_position, rocker_axis, rocker_angle)

    # Get pushrod position
    def get_pushrod_position(self):
        pushrod_position = self._pushrod_position
        return pushrod_position

    # Get damper position
    def get_damper_position(self):
        damper_position = self._damper_position
        return damper_position

    # Update Rocker rotation
    def update(self, rocker_angle):
        # Update pushrod position
        self.set_pushrod_position(rocker_angle)
        # Update damper position
        self.set_damper_position(rocker_angle)
