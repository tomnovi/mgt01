import numpy as np

x = np.array([1, 0, 0])

y = x / np.linalg.norm(x) if np.linalg.norm(x) > 1.0 else x

print(x)
print(y)
