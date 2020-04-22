import numpy as np
from utilities import rotation_matrix

class Wheel:

    # Define constructor with all class parameters
    def __init__(self, **kwargs):
        self.upper_wishbone_position = kwargs["upper_wishbone"] if "upper_wishbone" in kwargs else None
        self.lower_wishbone_position = kwargs["lower_wishbone"] if "lower_wishbone" in kwargs else None
        self.pushrod_position = kwargs["pushrod"] if "pushrod" in kwargs else None
        self.trackrod_position = kwargs["trackrod"] if "trackrod" in kwargs else None
        self.wheel_centre = kwargs["wheel_centre"] if "wheel_centre" in kwargs else None
        self.body_centre = self.wheel_centre
        self._wheel_travel = {"longitudinal": 0, "lateral": 0, "vertical": 0, "camber": 0, "castor": 0, "toe": 0}

        # Instatiate objects
        self.Rotation = rotation_matrix.RotationMatrix()

        # Define fixed arm lenghts of pickup points respect to wheel centre
        self.wheel_centre_2_upper_wishbone = self.upper_wishbone_position - self.wheel_centre
        self.wheel_centre_2_lower_wishbone = self.lower_wishbone_position - self.wheel_centre
        self.wheel_centre_2_pushrod = self.pushrod_position - self.wheel_centre
        self.wheel_centre_2_trackrod = self.trackrod_position - self.wheel_centre

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

        # Defining array with arms respect to wheel centre
        wheel_pickups = np.array([self.wheel_centre_2_upper_wishbone, self.wheel_centre_2_lower_wishbone, self.wheel_centre_2_pushrod, self.wheel_centre_2_trackrod])

        # Local vector with wheel translations
        wheel_translations = np.array([self._wheel_travel["longitudinal"], self._wheel_travel["lateral"], self._wheel_travel["vertical"]])
        self.wheel_centre = self.body_centre + wheel_translations

        # Perform rigid body rotation
        pickups_positions = np.matmul(wheel_pickups, np.matmul(np.matmul(self.R["A"], self.R["B"]), self.R["C"])) + wheel_translations + self.body_centre

        # Update pickup points location in object
        self.upper_wishbone_position = pickups_positions[0, :]
        self.lower_wishbone_position = pickups_positions[1, :]
        self.pushrod_position = pickups_positions[2, :]
        self.trackrod_position = pickups_positions[3, :]

    # Set pickup point derivative with respect to wheel movement
    def set_dpickups_dswheel(self):
        # Start by defining array with arms respect to wheel centre
        wheel_pickups = np.array([self.wheel_centre_2_upper_wishbone, self.wheel_centre_2_lower_wishbone, self.wheel_centre_2_pushrod, self.wheel_centre_2_trackrod])

        # Get the rotation matrix first derivative
        self.dR = Rotation.first()

        self.drpickups_dswheel_long = np.array([1, 0, 0])
        self.drpickups_dswheel_lat = np.array([0, 1, 0])
        self.drpickups_dswheel_vert = np.array([0, 0, 1])
        self.drpickups_dswheel_camb = np.matmul(wheel_pickups, np.matmul(self.A, np.matmul(self.B, self.C)))
        self.drpickups_dswheel_cast = np.matmul(wheel_pickups, np.matmul(self.A, np.matmul(self.B, self.C)))
        self.drpickups_dswheel_toe = np.matmul(wheel_pickups, np.matmul(self.A, np.matmul(self.B, self.dC)))
