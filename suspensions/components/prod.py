from .rocker import Rocker

class Prod(Rocker):
    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        # Define public attributes
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None        # Define public attributes
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None
        Rocker.__init__(self)

        self.prod_position = kwargs["prod"] if "prod" in kwargs else None

        # Instiate rodrigues objects
        self.prod_rotation = rodrigues.Rodrigues(pivot_position=self.pivot_position, pickup_position=self.prod_position, rotation_axis=self.rocker_axis)

    # Rotation to pushrod
    def apply_rotation(self):
        self.rocker_travel += self._rocker_angle
        self.prod_position = self.pushrod_rotation.rotation(self._rocker_angle)
        self.dpushrod_drocker = self.pushrod_rotation.first_derivative(self._rocker_angle)
