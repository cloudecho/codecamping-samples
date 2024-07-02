import matplotlib.pyplot as plt
import numpy as np

count = 200

z = np.linspace(-3, 3, count)
r = z**2 + 2
theta = np.linspace(-6 * np.pi, 6 * np.pi, count)
x = r * np.sin(theta)
y = r * np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(x, y, z, label="3D Line Plot")

plt.show()
