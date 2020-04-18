import numpy as np
import matplotlib.pyplot as plt
import quartersusp.rocker as rocker

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

# Define rocker pivot pickup points
r_rocker1 = np.array([0.44368, 0.23558, 0.56372])
r_rocker2 = np.array([0.47568, 0.23558, 0.56372])
r_rocker = np.array([0.4579, 0.23558, 0.56372])

# Define wheel center location
r_wheel_ctr = np.array([0.445, 0.59, 0.229])

# Define damper pickup points
r_damper_rocker = np.array([0.45975, 0.2163, 0.6453])
r_damper_frame = np.array([0.45968, 0.054, 0.5801])

################################################################################
################################################################################
# TEST CODE
Rocker = rocker.Rocker(pivot=r_rocker, pushrod=r_prod_out, damper=r_damper_rocker, axis1=r_rocker1, axis2=r_rocker2)
p = Rocker.get_pushrod_position()
plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(*zip(r_rocker, p), c='r')

a_rocker = 10 * np.pi / 180
for i in range(0,36):
    Rocker.update(a_rocker)
    p = Rocker.get_pushrod_position()
    ax.plot3D(*zip(r_rocker, p), c='b')

plt.show()

def run():
    print("Hello World")
