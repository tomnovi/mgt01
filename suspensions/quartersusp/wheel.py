import numpy as np
import numpy.matlib

class Wheel:

    # Define constructor with all class parameters
    def __init__(self):
        self._upper_wishbone_position = kwargs["upper_wishbone"] if "upper_wishbone" in kwargs else None
        self._lower_wishbone_position = kwargs["lower_wishbone"] if "lower_wishbone" in kwargs else None
        self._pushrod_position = kwargs["pushrod"] if "pushrod" in kwargs else None
        self._trackrod_position = kwargs["trackrod"] if "trackrod" in kwargs else None
        self._wheel_centre = kwargs["wheel_centre"] if "wheel_centre" in kwargs else None
        self._body_centre = self._wheel_centre

        # Define fixed arm lenghts of pickup points respect to wheel centre
        self._wheel_centre_2_upper_wishbone = self._upper_wishbone_position - self._wheel_centre
        self._wheel_centre_2_lower_wishbone = self._lower_wishbone_position - self._wheel_centre
        self._wheel_centre_2_pushrod = self._pushrod_position - self._wheel_centre
        self._wheel_centre_2_trackrod = self._trackrod_position - self._wheel_centre

    # Update rotation matrix of the rigid body
    def set_rotation_matrix(self, s_wheel):
        # Apply this transformation to the main body.
        sa = np.sin(s_wheel["camber"])
        ca = np.cos(s_wheel["camber"])
        sb = np.sin(s_wheel["castor"])
        cb = np.cos(s_wheel["castor"])
        sc = np.sin(s_wheel["toe"])
        cc = np.cos(s_wheel["toe"])

        # Define rotation matrix - Roll (Camber), Pitch (Caster) , Yaw (Toe)
        self._A = np.array([[1, 0, 0], [0, ca, sa], [0, -sa, ca]])
        self._B = np.array([[cb, 0, -sb], [0, 1, 0], [sb, 0, cb]])
        self._C = np.array([[cc, sc, 0], [-sc, cc, 0], [0, 0, 1]])

        # Define first derivative or ration matrix
        self._dA = np.array([[0, 0, 0], [0, -sa, ca], [0, -ca, -sa]])
        self._dB = np.array([[-sb, 0, -cb], [0, 0, 0], [cb, 0, -sb]])
        self._dC = np.array([[-sc, cc, 0], [-cc, -sc, 0], [0, 0, 0]])

    # Set pickup points of wheel after movement of the wheel
    def set_pickups_position(self, s_wheel):
        # Define local arrays to make calculation more efficient
        # Start by defining array with arms respect to wheel centre
        wheel_pickups = np.array([self._wheel_centre_2_upper_wishbone, self._wheel_centre_2_lower_wishbone, self._wheel_centre_2_pushrod, self._wheel_centre_2_trackrod])

        # Local vector with wheel translations
        wheel_translations = np.array([s_wheel["longitudinal"], s_wheel["lateral]"], s_wheel["vertical"]])

        # Perform rigid body rotation
        pickups_positions = np.matmul(wheel_pickups, np.matmul(np.matmul(self._A, self._B), self._C)) + wheel_translations + self._body_centre

        # Update pickup points location in object
        self._upper_wishbone_position = pickups_positions[1, :]
        self._lower_wishbone_position = pickups_positions[2, :]
        self._pushrod_position = pickups_positions[3, :]
        self._trackrod_position = pickups_positions[4, :]

    # Set pickup point derivative with respect to wheel movement
    def set_dpickups_dswheel(self, s_wheel):
        # Start by defining array with arms respect to wheel centre
        wheel_pickups = np.array([self._wheel_centre_2_upper_wishbone, self._wheel_centre_2_lower_wishbone, self._wheel_centre_2_pushrod, self._wheel_centre_2_trackrod])

        self._drpickups_dswheel_long = np.array([1, 0, 0])
        self._drpickups_dswheel_lat = np.array([0, 1, 0])
        self._drpickups_dswheel_vert = np.array([0, 0, 1])
        self._drpickups_dswheel_camb = np.matmul(wheel_pickups, np.matmul(self._dA, np.matmul(self._B, self._C)))
        self._drpickups_dswheel_cast = np.matmul(wheel_pickups, np.matmul(self._A, np.matmul(self._B, self._C)))
        self._drpickups_dswheel_toe = np.matmul(wheel_pickups, np.matmul(self._A, np.matmul(self._B, self._dC)))

    # Getter for pickup points
    def get_pickups_position(self):
        pickups_position = {
        "upper_wishbone": self._upper_wishbone_position,
        "lower_wishbone": self._lower_wishbone_position,
        "pushrod_wishbone": self._pushrod_position,
        "trackrod_wishbone": self._trackrod_position,
        }

        return pickups_position

    # Getter for rotation matrix
    def get_rotation_matrix(self):
        rotation_matrix = {
        A: self._A,
        B: self._B,
        C: self._C,
        dA: self._dA
        dB: self._dB
        dC: self._dC
        }

        return rotation_matrix

    # Update pickup points
    def update(self, s_wheel):
        # Update rotation matrix
        self.set_rotation_matrix(s_wheel)
        # Update pickup position
        self.set_pickups_position(s_wheel)
        # Update pickup points derivatives wrt wheel positions
        self.set_dpickups_dswheel(s_wheel)
