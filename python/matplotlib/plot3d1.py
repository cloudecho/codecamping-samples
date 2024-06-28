import matplotlib.pyplot as plt
import numpy as np

# xpoints, ypoints , zpoints
size = (10)
x = np.random.randint(10, size=size)
y = np.random.randint(10, size=size)
z = np.random.randint(10, size=size)
print('x ', x)
print('y ', y)
print('z ', z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='g', marker='^')

ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')

plt.show()

