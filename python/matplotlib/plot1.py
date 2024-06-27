import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

# draw a line from 
# (x1, y1) -> (x2, y2)
# e.g.
# (0, 1) -> (6, 7)
xpoints = np.array([0, 6])
ypoints = np.array([1, 7])

print('xpoints', xpoints)
print('ypoints', ypoints)

plt.plot(xpoints, ypoints, 'o:r')
plt.show()

