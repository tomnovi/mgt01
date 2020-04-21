import numpy as np

class Rodrigues():
    def __init__(self, **kwargs):
        # Set constants
        self.er = kwargs["rotation_axis"] / np.linalg.norm(kwargs["rotation_axis"]) if "rotation_axis" in kwargs else None
        self.v0 = kwargs["pivot_position"] if "pivot_position" in kwargs else None
        self.v1 = kwargs["pickup_position"] - self.v0 if "pickup_position" in kwargs else None
        self.v2 = np.cross(self.er, self.v1)
        self.v3 = self.er * np.inner(self.er, self.v1)

    def rotation(self, angle):
        # Perform Rodriues rotation
        self.v1 = self.v1*np.cos(angle) + self.v2*np.sin(angle) - self.v3*(1-np.cos(angle))
        self.v2 = np.cross(self.er, self.v1)
        self.v3 = self.er * np.inner(self.er, self.v1)
        vrot = self.v1 + self.v0
        return vrot

    def first_derivative(self, angle):
        # Calculate first derivative
        dvrot_dangle = -self.v1*np.sin(angle) + self.v2*np.cos(angle) + self.v3*np.sin(angle)
        return dvrot_dangle
