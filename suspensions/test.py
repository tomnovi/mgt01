from utilities import rodrigues
import numpy as np
import matplotlib.pyplot as plt

axis = np.array([1, 0, 0])
pickup = np.array([1, 1, 0])
pivot = np.array([1, 0, 0])
Rodrigues = rodrigues.Rodrigues(pivot_position=pivot, pickup_position=pickup, rotation_axis=axis)

plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(*zip(pivot, pickup), c='r')
angle = 10 * np.pi / 180

for i in range(0,35):#
    vrot = Rodrigues.rotation(angle)
    ax.plot3D(*zip(pivot, vrot), c='b')
plt.show()
