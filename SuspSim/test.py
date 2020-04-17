import numpy as np
import matplotlib.pylab as plt

data = np.load('SuspSim/mat.npz')

lDamper = data["Damper_Length"][:, 0] if data["Wheel_Vertical_Travel"] > 0
zWheel = data["Wheel_Vertical_Travel"] if data["Wheel_Vertical_Travel"] > 0

print(lDamper.shape)
print(zWheel.shape)

ir = np.divide(np.diff(lDamper), np.diff(zWheel))

plt.figure()
plt.plot(zWheel, lDamper)
plt.show()
