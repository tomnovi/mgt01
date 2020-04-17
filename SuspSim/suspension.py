from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib


# Define functions
def get_geometry():
    # Outboard pickup points
    r_uwbf_out = np.array([0.462, 0.484, 0.323])
    r_uwbr_out = np.array([0.462, 0.484, 0.323])
    r_lwbf_out = np.array([0.447, 0.53, 0.138])
    r_lwbr_out = np.array([0.447, 0.53, 0.138])
    r_prod_out = np.array([0.4579, 0.4497, 0.3349])
    r_trod_out = np.array([0.398, 0.53, 0.156])

    # Inboard pickup points
    r_uwbf_in = np.array([0.295, 0.2515, 0.274])
    r_uwbr_in = np.array([0.55, 0.2755, 0.272])
    r_lwbf_in = np.array([0.415, 0.2245, 0.13])
    r_lwbr_in = np.array([0.57, 0.251, 0.144])
    r_prod_in = np.array([0.4597, 0.3196, 0.5609])
    r_trod_in = np.array([0.334, 0.225, 0.14])

    # Define matrix of pickup points
    r_out = np.vstack((r_uwbf_out, r_uwbr_out, r_lwbf_out, r_lwbr_out, r_prod_out, r_trod_out))
    r_in = np.vstack((r_uwbf_in, r_uwbr_in, r_lwbf_in, r_lwbr_in, r_prod_in, r_trod_in))

    # Define rocker pivot pickup points
    r_rocker1 = np.array([0.44368, 0.23558, 0.56372])
    r_rocker2 = np.array([0.47568, 0.23558, 0.56372])
    r_rocker = (r_rocker1 + r_rocker2)/2

    # Define wheel center location
    r_wheel_ctr = np.array([0.445, 0.59, 0.229])

    # Define damper pickup points
    r_damper_rocker = np.array([0.45975, 0.2163, 0.6453])
    r_damper_frame = np.array([0.45968, 0.054, 0.5801])

    # Define all damper points in one vector
    r_damper = np.vstack((r_damper_rocker, r_damper_frame))

    # Define a dictionary with all pickup points
    r = {
        "Inner": r_in,
        "Outer": r_out,
        "Rocker": r_rocker,
        "Damper": r_damper,
        "Wheel": r_wheel_ctr,
    }

    # Define output of function
    return r


def get_rocker_axis(r):

    # Start by calculating rocker rotation axis
    rr = np.cross(r["Inner"][4, :] - r["Rocker"], r["Outer"][4, :] - r["Inner"][4, :])
    r_rocker1 = np.array([0.44368, 0.23558, 0.56372])
    r_rocker2 = np.array([0.47568, 0.23558, 0.56372])
    rr2 = r_rocker1 - r_rocker2
    er2 = rr2 / np.linalg.norm(rr2)
    er = rr / np.linalg.norm(rr)

    # Write output
    return er2


def get_new_inner_pickups(r, er, a_rocker, s_rack):

    # The Rocker position can be found with the Rodrigues rotation and the rack with a simple y displacement
    # Perform Rodrigues rotation
    rArm = r["Inner"][4, :] - r["Rocker"]
    sa = np.sin(a_rocker)
    ca = np.cos(a_rocker)
    r["Inner"][4, :] = rArm * ca + np.cross(er, rArm) * sa + er * np.inner(er, rArm) * (1 - ca) + r["Rocker"]

    # Move th rack in the y direction
    r["Inner"][5, :] = r["Inner"][5, :] + [0, s_rack, 0]

    # Calculate first derivative
    dr_darocker = - rArm * sa + np.cross(er, rArm) * ca + er * np.inner(er, rArm) * sa
    dr_dsrack = np.array([0, 1, 0])

    # Write output
    return r, dr_darocker, dr_dsrack


def get_rotation_matrix(s):
    # Apply this transformation to the main body.
    sa = np.sin(s[3])
    ca = np.cos(s[3])
    sb = np.sin(s[4])
    cb = np.cos(s[4])
    sc = np.sin(s[5])
    cc = np.cos(s[5])

    # Define rotation matrix - Roll (Camber), Pitch (Caster) , Yaw (Toe)
    A = np.array([[1, 0, 0], [0, ca, sa], [0, -sa, ca]])
    B = np.array([[cb, 0, -sb], [0, 1, 0], [sb, 0, cb]])
    C = np.array([[cc, sc, 0], [-sc, cc, 0], [0, 0, 1]])

    # Define first derivative or ration matrix
    dA = np.array([[0, 0, 0], [0, -sa, ca], [0, -ca, -sa]])
    dB = np.array([[-sb, 0, -cb], [0, 0, 0], [cb, 0, -sb]])
    dC = np.array([[-sc, cc, 0], [-cc, -sc, 0], [0, 0, 0]])

    # Write out your exit structure
    R = {
        "A": A,
        "B": B,
        "C": C,
        "dA": dA,
        "dB": dB,
        "dC": dC,
    }

    return R


def get_rigid_body_displacement(s, r, r0, r_r0):

    # Get rotation matrix
    R = get_rotation_matrix(s)

    # Perform the rotation and translation of the hub and calculate the position of the pickup points on the hub
    r["Outer"] = np.matmul(r_r0, np.matmul(np.matmul(R["A"], R["B"]), R["C"])) + s[:3] + r0

    # Write output
    return r, R


def get_error(r, l):
    # Compute the radius error – how far rPickupsOut are from the pivot of each motor – this should equal the legs.
    # This is a [6x3] matrix, rows are leg and columns are direction (x,y,z)
    d = r["Outer"] - r["Inner"]

    # Calculate vector of errors - difference of squared lengths [6x1]
    error = np.sum(np.abs(d) ** 2, axis=-1) - l

    return error, d


def get_error_jacobian_swheel(d, r_r0, R):

    # We want to calculate derr_dsWheelCtr so we can then use Newton-Raphson steps to solve for sWheelCtr.
    # derr_dsWheelCtr = 2 * dot(rLegs , drLegs_dsWheelCtr); [6x6]
    # And we can simply because
    # drLegs_dsWheelCtr = drPickupsOut_dsWheelCtr; [6x3]
    dr_ds0 = np.matlib.repmat([1, 0, 0], 6, 1)
    dr_ds1 = np.matlib.repmat([0, 1, 0], 6, 1)
    dr_ds2 = np.matlib.repmat([0, 0, 1], 6, 1)
    dr_ds3 = np.matmul(r_r0, np.matmul(R["dA"], np.matmul(R["B"], R["C"])))
    dr_ds4 = np.matmul(r_r0, np.matmul(R["A"], np.matmul(R["dB"], R["C"])))
    dr_ds5 = np.matmul(r_r0, np.matmul(R["A"], np.matmul(R["B"], R["dC"])))

    derr_ds0 = 2 * np.einsum('ij,ij->i', d, dr_ds0)
    derr_ds1 = 2 * np.einsum('ij,ij->i', d, dr_ds1)
    derr_ds2 = 2 * np.einsum('ij,ij->i', d, dr_ds2)
    derr_ds3 = 2 * np.einsum('ij,ij->i', d, dr_ds3)
    derr_ds4 = 2 * np.einsum('ij,ij->i', d, dr_ds4)
    derr_ds5 = 2 * np.einsum('ij,ij->i', d, dr_ds5)

    # Compose the derr_dsWheelCtr array
    derr_ds = np.vstack((derr_ds0, derr_ds1, derr_ds2, derr_ds3, derr_ds4, derr_ds5))
    derr_ds = derr_ds.transpose()

    # Write output
    return derr_ds


def get_error_jacobian_spickupsin(d, dr_darocker, dr_dsrack):

    # We want to calculate derr_dsPickupsin so we can then find the installation ratio.
    # derr_dsPickupsIn = 2 * dot(rLegs , drLegs_dsPickupsIn; [6x6]
    # Where:
    # drLegs_dsPickupsIn = - drPickupsIn_dsWheelCtr; [6x6]

    # Fill element [4, 4] with pushrod length error due to rocker rotation
    derr_darocker = np.array([0, 0, 0, 0, -2 * np.inner(d[4, :], dr_darocker), 0])

    # Fill element [5, 5] with tierod length error due to rack displacement
    derr_dsrack = np.array([0, 0, 0, 0, 0, -2 * np.inner(d[5, :], dr_dsrack)])

    # Write output
    return derr_darocker, derr_dsrack


def get_damper_jacobian_arocker(r, er, a_rocker):

    # The Rocker position can be found with the Rodrigues rotation and the rack with a simple y displacement
    # Perform Rodrigues rotation
    rArm = r["Damper"][0, :] - r["Rocker"]
    sa = np.sin(a_rocker)
    ca = np.cos(a_rocker)
    r["Damper"][0, :] = (rArm) * ca + np.cross(er, rArm) * sa + er * np.inner(er, rArm) * (1 - ca) + r["Rocker"]

    # Find the variation of damper pickup on the rocker as a function of rocker angle
    dr_darocker = - (rArm) * sa + np.cross(er, rArm) * ca + er * np.inner(er, rArm) * sa

    # Calculate unit vector for damper axis
    r_damper = r["Damper"][0, :] - r["Damper"][1, :]
    e_damper = r_damper / np.linalg.norm(r_damper)

    # The variation of the damper length as a function of rocker rotation is simply the dot product between the
    # variation of damper pickup on the rocker as a function or rocker angle and the direction of the damper unit vector
    dr_ds = np.inner(dr_darocker, e_damper)

    # Write output
    return dr_ds


# Get geometry of suspension
rPickups = get_geometry()


eRocker = get_rocker_axis(rPickups)

# Define position to which reference all measurements (Wheel centre in design condition?)
rBodyCentre = np.copy(rPickups["Wheel"])

# Define leg lengths
lLegs2 = np.sum(np.abs(rPickups["Outer"] - rPickups["Inner"]) ** 2, axis=-1)

# Define Rocker arms
lRockerPRODIn = np.linalg.norm(rPickups["Inner"][4, :] - rPickups["Rocker"])

# Define rPickupsOut_wheelCtr (points R external pickup points in wheel local frame)
rPickupsOut_wheelCtr = rPickups["Outer"] - rPickups["Wheel"]

# Initialise displacement vector of wheel center
sWheelCtr = np.zeros(6)

# Initialise total rocker angle and rack displacement
aRocker = 0
sRack = 0

# Define rocker and rack displacement
daRocker = 1 * np.pi / 180
dsRack = 0 * 1e-03
lDamper = np.linalg.norm(rPickups["Damper"][0, :] - rPickups["Damper"][1, :])
zWheel = 0

for i in range(0, 30):

    # Update total displacement of rack and rocker
    aRocker += daRocker
    sRack += dsRack

    # Calculate new position of inner pickups
    rPickups, drPRODIn_daRocker, drTRODIn_dsRack = get_new_inner_pickups(
        rPickups, eRocker, daRocker, dsRack)
    a = np.copy(sWheelCtr)
    # Loop to find solution
    for i in range(0, 3):

        # Calculate new position of outer pickups
        rPickups, R = get_rigid_body_displacement(
            sWheelCtr, rPickups, rBodyCentre, rPickupsOut_wheelCtr)

        # Calculate error
        err, rLegs = get_error(rPickups, lLegs2)

        # Get error Jacobian wrt sWheelCtr
        derr_dsWheelCtr = get_error_jacobian_swheel(rLegs, rPickupsOut_wheelCtr, R)

        # Perform Newton Raphson steps
        sWheelCtr = sWheelCtr - np.matmul(np.linalg.inv(derr_dsWheelCtr), err)

        # Calculate error Jacobian wtr sPickupsIn
        derr_daRocker, derr_dsRack = get_error_jacobian_spickupsin(
            rLegs, drPRODIn_daRocker, drTRODIn_dsRack)

    # Calculate Jacobian of sWheelCtr wrt sPickupsIn
    dsWheelCtr_daRocker = - np.matmul(np.linalg.inv(derr_dsWheelCtr), derr_daRocker)
    dsWheelCtr_dsRack = - np.matmul(np.linalg.inv(derr_dsWheelCtr), derr_dsRack)

    # Calculate Jacobiano of sDamper wrt to sRocker
    dsDamper_daRocker = get_damper_jacobian_arocker(rPickups, eRocker, daRocker)
