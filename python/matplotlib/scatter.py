import matplotlib.pyplot as plt
import numpy as np


count = 50
max_val = 10

x = np.random.randint(max_val, size=(count))
y = np.random.randint(max_val, size=(count))
colors = np.random.randint(100, size=(count))
sizes = np.random.randint(2000, size=(count))

print('count', count)
print('x', x)
print('y', y)
print('colors', colors)
print('sizes', sizes)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.colorbar()
plt.show()