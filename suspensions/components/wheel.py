import numpy as np
from utilities import rotation_matrix

class Wheel():

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        self.ufront_position = kwargs["upper_front"] if "upper_front" in kwargs else None
        self.urear_position = kwargs["upper_rear"] if "upper_rear" in kwargs else None
        self.lfront_position = kwargs["lower_front"] if "lower_front" in kwargs else None
        self.lrear_position = kwargs["lower_rear"] if "lower_rear" in kwargs else None
        self.prod_position = kwargs["pushrod"] if "pushrod" in kwargs else None
        self.trod_position = kwargs["trackrod"] if "trackrod" in kwargs else None
        self.wheel_centre = kwargs["wheel_centre"] if "wheel_centre" in kwargs else None
        self.body_centre = self.wheel_centre
        self.wheel_pickups = np.subtract([self.ufront_position, self.urear_position, self.lfront_position, self.lrear_position , self.prod_position, self.trod_position], self.wheel_centre)

        # Define private class attributes
        self._wheel_travel = {"longitudinal": 0, "lateral": 0, "vertical": 0, "camber": 0, "castor": 0, "toe": 0}

        # Instatiate objects
        self.Rotation = rotation_matrix.RotationMatrix()


    @property
    def wheel_displacement(self):
        return self._wheel_travel

    @wheel_displacement.setter
    def wheel_displacement(self, value):
        self._wheel_travel = value

    # Set pickup points of wheel after movement of the wheel
    def apply_displacement(self):
        # Get the rotation matrices
        self.R = self.Rotation.rotation([self._wheel_travel["camber"], self._wheel_travel["castor"], self._wheel_travel["toe"]])
        self.dR = self.Rotation.first_derivative()

        # Local vector with wheel translations
        wheel_translations = np.array([self._wheel_travel["longitudinal"], self._wheel_travel["lateral"], self._wheel_travel["vertical"]])
        self.wheel_centre = self.body_centre + wheel_translations

        # Perform rigid body rotation
        pickups_positions = np.matmul(self.wheel_pickups, np.matmul(np.matmul(self.R["A"], self.R["B"]), self.R["C"])) + wheel_translations + self.body_centre

        # Update pickup points location in object
        self.ufront_position = pickups_positions[0, :]
        self.urear_position = pickups_positions[1, :]
        self.lfront_position = pickups_positions[2, :]
        self.lrear_position = pickups_positions[3, :]
        self.prod_position = pickups_positions[4, :]
        self.trod_position = pickups_positions[5, :]

        # Get the first derivative of pickups wrt to wheel displacement
        self.first_derivative()

    def first_derivative(self):
        dpickups_dwheel_long = np.array([1, 0, 0])
        dpickups_dwheel_lat = np.array([0, 1, 0])
        dpickups_dwheel_vert = np.array([0, 0, 1])
        dpickups_dwheel_camb = np.matmul(self.wheel_pickups, np.matmul(self.dR["dA"], np.matmul(self.R["B"], self.R["C"])))
        dickups_dwheel_cast = np.matmul(self.wheel_pickups, np.matmul(self.R["A"], np.matmul(self.dR["dB"], self.R["C"])))
        dpickups_dwheel_toe = np.matmul(self.wheel_pickups, np.matmul(self.R["A"], np.matmul(self.R["B"], self.dR["dC"])))

        self.dpickups_dwheel = [dpickups_dwheel_long, dpickups_dwheel_lat, dpickups_dwheel_vert, dpickups_dwheel_camb, dpickups_dwheel_cast, dpickups_dwheel_toe]
