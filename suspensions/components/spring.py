from .rocker import Rocker

class Spring(Rocker):
    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        # Define public attributes
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None        # Define public attributes
        self.pivot_position = kwargs["pivot"] if "pivot" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None
        self.rocker_axis = (kwargs["axis1"] - kwargs["axis2"]) if "axis1" and "axis2" in kwargs else None
        Rocker.__init__(self)

        self.damper_position = kwargs["damper"] if "damper" in kwargs else None

        # Instiate rodrigues objects
        self.damper_rotation = rodrigues.Rodrigues(pivot_position=self.pivot_position, pickup_position=self.damper_position, rotation_axis=self.rocker_axis)

    # Rotation to pushrod
    def apply_rotation(self):
        self.rocker_travel += self._rocker_angle
        self.damper_position = self.damper_rotation.rotation(self._rocker_angle)
        self.ddamper_drocker = self.damper_rotation.first_derivative(self._rocker_angle)
