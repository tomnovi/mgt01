import numpy as np

# Define the Rodrigues rotation method
def rodrigues_rotation(pickup_position, pivot_position, rotation_unit_axis, rotation_angle):

    # Check if rotation axis is a unit vector, if not normalise
    er = rotation_unit_axis / np.linalg.norm(rotation_unit_axis) if np.linalg.norm(rotation_unit_axis) > 1.0 else rotation_unit_axis

    # Condens sine and cosine of angle
    sa = np.sin(rotation_angle)
    ca = np.cos(rotation_angle)

    # Condens vectors to rotate
    v0 = pivot_position
    v1 = pickup_position - pivot_position
    v2 = np.cross(er, v1)
    v3 = er * np.inner(er, v1)

    # Perform Rodriues rotation
    pickup_position = v1*ca + v2*sa - v3*(1-ca) + v0

    # Calculate first derivative
    dpickup_position_drotation_angle = -v1*sa + v2*ca + v3*sa

    # Write outputs
    return pickup_position
