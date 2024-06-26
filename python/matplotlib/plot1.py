import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

print('xpoints', xpoints)
print('ypoints', ypoints)

plt.plot(xpoints, ypoints)
plt.show()

